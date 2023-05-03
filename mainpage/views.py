from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import  Patient, Take_Turn,Services,Reception,day_of
from reception.models import refer_to_surgery
from .forms import patientEditForm, Searchbox, patientTotalForm,day_ofEditForm,Filter_form
from datetime import datetime,date, timedelta,timezone
import pytz
from jalali_date import date2jalali
from account.check_user import chech_profile
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import django_excel as excel
from pyexcel_xlsx import save_data
from persiantools.jdatetime import JalaliDate
import datetime as DATE
#import datetime
# Create your views here.

@login_required
def Home (request):
    now=datetime.now()
    tz = pytz.timezone('Asia/Tehran')
    xc=tz.localize(datetime(now.year, now.month, now.day))

    x =Take_Turn.objects.filter(date_time__date=xc)

    return render(request, "main/home.html",{'turn':x})
@login_required
def patient_file(request, id):
    try:
        patient = get_object_or_404(Patient, id=id)
    except:
        patient = get_object_or_404(Patient, pk=id)
    if request.method == 'POST':

        if request.POST.get("NationalCode") != None:
            patient.NationalCode = request.POST.get("NationalCode")
        if request.POST.get('p_name') != None:
            patient.p_name = request.POST.get('p_name')
        if request.POST.get('last_name') != None:
            patient.last_name=request.POST.get('last_name')
        if request.POST.get('mobile') != None:
            patient.mobile=request.POST.get('mobile')
        if request.POST.get('land_line_phone') != None:
            patient.land_line_phone=request.POST.get('land_line_phone')
        if request.POST.get('age') != None and request.POST.get('age') != '':
            patient.age=request.POST.get('age')
        if request.POST.get('Gender') != None and request.POST.get('Gender') != '':
            patient.Gender=request.POST.get('Gender')
        patient.save()
        return redirect(patient)


    else:
        active_turn = []
        deactive_turn = []
        tz = pytz.timezone('Asia/Tehran')
        this_p_turn = Take_Turn.objects.filter(Patient=patient)

        for i in this_p_turn:
            if tz.localize(datetime.now())> i.date_time:
                deactive_turn.append(i)
            else:
                active_turn.append(i)
        reception =Reception.objects.filter(Patient=patient)
        patient_surgery=refer_to_surgery.objects.filter(Patient=patient)
        patientedit = patientEditForm(instance=patient)
        return render(request,'main/detail.html',{'patient': patient,'patientedit':patientedit,'deactive_turn':deactive_turn,'active_turn':active_turn,'reception':reception,'surgery':patient_surgery})
@login_required
def creatFile(request):
    user = request.user
    x = chech_profile(user, 13)
    if x == True:
        if request.method == 'POST':
            form = patientTotalForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                x=Patient.objects.create(NationalCode=cd['NationalCode'],
                p_name=cd['p_name'],
                last_name=cd['last_name'],
                mobile=cd['mobile'],
                land_line_phone=cd['land_line_phone'],
                age=cd['age'],
                Gender=cd['Gender'],
                )

                return redirect(x)
        form =patientTotalForm()
        return render(request,'main/create.html',{'form':form })
    else:
        return render(request, 'main/error.html',{'mess':'دسترسی ایجاد پرونده برای شما فعال نشده است.'})


def searchb_us (request):
    if request.method == 'POST':
        form = Searchbox(request.POST)
        if request.POST.get('status') == '1':
            if form.is_valid():

                text =form.cleaned_data['searchtxt']
                patient = Patient.objects.all()
                q1 = patient.filter(Q(p_name__icontains=text))
                q2 = patient.filter(Q(last_name__icontains=text))
                q3 = patient.filter(Q(NationalCode__icontains=text))
                q4 = patient.filter(Q(mobile__icontains=text))
                item = (q1 | q2 | q3 | q4).order_by('-id')
                print(item)
                return render(request, 'main/search_result.html',{'patient':item,'searchform':Searchbox})
        elif request.POST.get('status') == '2':
            if form.is_valid():
                text =form.cleaned_data['searchtxt']
                reception = Reception.objects.all()
                q1 = reception.filter(Q(EntranceCode__icontains=text))
                q2 = reception.filter(Q(TurnCode__icontains=text))
                q3 = reception.filter(Q(Referrer__icontains=text))
                item = (q1 | q2 | q3 ).order_by('-id')
                return render(request, 'main/search_result.html',{'reception':item})
        elif request.POST.get('status') == '3':
            if form.is_valid():
                text =form.cleaned_data['searchtxt']
                refer = refer_to_surgery.objects.all()
                #q1 = refer.filter(Q(Patient__icontains=text))
                q2 = refer.filter(Q(name__icontains=text))
                q3 = refer.filter(Q(name_Doc__icontains=text))
                #q4 = refer.filter(Q(name__icontains=text))
                #q5 = refer.filter(Q(name_Doc__icontains=text))
                item = ( q2 | q3 ).order_by('-id')
                return render(request, 'main/search_result.html',{'refer':item})
        elif request.POST.get('status') == '4':
            if form.is_valid():
                text =form.cleaned_data['searchtxt']
                turn = Take_Turn.objects.all().filter(Patient__NationalCode__icontains=text)
                turns_list = Take_Turn.objects.all().filter(Patient__NationalCode__icontains=text)
                # patient = Patient.objects.all()
                # q1 = patient.filter(Q(NationalCode__icontains=text))
                # turns_list = []
                # for i in q1:
                #     for j in turn:
                #         if j.Patient == i:
                #             turns_list.append(j)


                #item = ( q2 | q3 ).order_by('-id')
                return render(request, 'main/search_result.html',{'turns':turns_list})
    else:
        return HttpResponse('Invalid Method')
def pationt_list(request):
    patient = Patient.objects.order_by('-id')

    p = Paginator(patient, 50)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    return render(request, 'main/patient_list.html',{'patient':page_obj})

#from collections import OrderedDict
def download(request):
    patient = Patient.objects.order_by('-id')
    patients_list = [[ 'نام',
     'نام خانوادگی',
      'كد ملی',
      'موبایل',
       'سن']]
    #data = OrderedDict()
    for i in patient:
        p_list =[i.p_name,i.last_name,i.NationalCode,i.mobile,i.age]
        patients_list.append(p_list)
    #data.update({"Sheet 1": patients_list})
    #sheet =save_data("your_file.xlsx", data)
    sheet = excel.pe.Sheet(patients_list)
    return excel.make_response(sheet, 'xlsx')
def surgery_list(request):
    surgery = refer_to_surgery.objects.order_by('-id')
    query_set = surgery
    if request.method == 'POST':
        getform = Filter_form(request.POST)
        if getform.is_valid():
            date1 =getform.cleaned_data['from_date']
            date2 =getform.cleaned_data['to_date']
            q1 = query_set.filter(Q(date_time__gte=date1))
            q2 = query_set.filter(Q(date_time__lte=date2))
            surgery = (q1 & q2).order_by('-id')
            form =Filter_form()
            return render(request, 'main/surgery_list.html',{'surgery':surgery,'form':form})
    form =Filter_form()
    return render(request, 'main/surgery_list.html',{'surgery':surgery,'form':form})

def download2(request):
    surgery = refer_to_surgery.objects.order_by('-id')
    patients_list = [['بیمار',
    'عنوان عمل',
    'نام پزشك',
    'وضعیت شرح حال',
    'وضعیت برائت نام',
    'تاریخ جراحی'
    ]]
    #data = OrderedDict()
    for i in surgery:
        if i.patient_history:
            a = "موجود است"
        else:
            a = "موجود نیست"
        if i.Medical_innocence:
            b = "موجود است"
        else:
            b = "موجود نیست"
        x= JalaliDate(DATE.date(i.date_time.year, i.date_time.month, i.date_time.day))
        p_list =[str(i.Patient),i.name,i.name_Doc,a,b,str(x)]
        patients_list.append(p_list)
    #data.update({"Sheet 1": patients_list})
    #sheet =save_data("your_file.xlsx", data)
    sheet = excel.pe.Sheet(patients_list)
    return excel.make_response(sheet, 'xlsx')
def Turn_list(request):
    turns = Take_Turn.objects.order_by('-id')
    query_set = turns
    if request.method == 'POST':
        getform = Filter_form(request.POST)
        if getform.is_valid():
            date1 =getform.cleaned_data['from_date']
            date2 =getform.cleaned_data['to_date']
            q1 = query_set.filter(Q(date_time__gte=date1))
            q2 = query_set.filter(Q(date_time__lte=date2))
            turns = (q1 & q2).order_by('-id')
            form =Filter_form()
            return render(request, 'main/turn_list.html',{'turns':turns,'form':form})
    form =Filter_form()
    return render(request, 'main/turn_list.html',{'turns':turns,'form':form})
def download3(request):
    turns = Take_Turn.objects.order_by('-id')
    turns_list = [[
    'بیمار',
    'شماره نوبت',
    'همكار',
    'بخش',
    'تاریخ نوبت ',
    'توضیحات'
    ]]
    #data = OrderedDict()
    for i in turns:
        part_choice = ['Post-مغز','post-کمر','post-هیپوفیز','new-مغز','new-کمر','new-هیپوفیز','بخیه-مغز','بخیه-کمر'
        ]
        part= part_choice[i.part]
        x= JalaliDate(DATE.date(i.date_time.year, i.date_time.month, i.date_time.day))
        t_list =[str(i.Patient),i.TurnCode,str(i.user),part,str(x),i.Description]
        turns_list.append(t_list)
    #data.update({"Sheet 1": patients_list})
    #sheet =save_data("your_file.xlsx", data)
    print(turns_list)
    sheet = excel.pe.Sheet(turns_list)
    return excel.make_response(sheet, 'xlsx')
def download4(request):
    res = Reception.objects.order_by('-id')
    turns_list = [[
    'مرحله',
    'بیمار',
    'کد پذیرش',
    'شماره نوبت',
    'تاریخ پذیرش',
    ]]
    #data = OrderedDict()
    for i in res:


        x= JalaliDate(DATE.date(i.date.year, i.date.month, i.date.day))
        t_list =[i.TypeTurn,str(i.Patient),i.EntranceCode,i.TurnCode,str(x)]
        turns_list.append(t_list)
    #data.update({"Sheet 1": patients_list})
    #sheet =save_data("your_file.xlsx", data)
    print(turns_list)
    sheet = excel.pe.Sheet(turns_list)
    return excel.make_response(sheet, 'xlsx')
def Calender (request):
    if request.method == 'POST':
        form = day_ofEditForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            day_of.objects.create(Description=cd['Description'],date_time=cd['date_time'])
        return redirect("main:Calender")
    form = day_ofEditForm()
    all_day_of = day_of.objects.all()
    list_day = []

    for i in all_day_of:
        if date.today()< i.date_time:
            list_day.append(i)
    today = date2jalali(date.today())

    return render(request, 'main/day_of.html',{'form':form,'lsit_day':list_day,'today':today})
