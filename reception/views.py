from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from .forms import ReceptionEditForm,paymentEditForm,PayReceiptEditForm,surgeryEditForm,refToSurgeryEditForm
from mainpage.models import Patient,Take_Turn,Services,Reception,PatientItem,Diagnosis,PatientDiagnosis,day_of
from .models import PaymentReceipt,refer_to_surgery
from django.contrib.auth.decorators import login_required
from jalali_date import date2jalali
from datetime import date as D
from datetime import datetime
from account.check_user import chech_profile
# Create your views here.
@login_required
def reception_form(request, id):
    user = request.user
    x = chech_profile(user, 12)
    if x == True:
        patient = get_object_or_404(Patient,id=id)
        mess = None
        alert = None
        if request.method == 'POST':
                reception = ReceptionEditForm(request.POST)
                if reception.is_valid():
                    cd =reception.cleaned_data
                    all_re = Reception.objects.all()
                    count = len(all_re)

                    entranceCode = count+1

                    try:
                        Rec=Reception.objects.create(Patient=patient,user=user,EntranceCode=entranceCode,TurnCode =cd['TurnCode'], date=cd['date'],Referrer=cd['Referrer'],Description=cd['Description'])
                        ListSercice =eval(cd['services'])
                        # ListD =eval(cd['diagnisis'])
                        L_ser = []
                        if type(ListSercice) == int:
                            ListSercice =(ListSercice,)
                        # if type(ListD) == int:
                            # ListD =(ListD,)
                        for i in ListSercice:
                            x=get_object_or_404(Services, id=i)
                            PatientItem.objects.create(Reception=Rec,Services=x,price=x.Price)
                            L_ser.append(x.Service)
                        # for i in ListD:
                            # y=get_object_or_404(Diagnosis, id=i)
                            # PatientDiagnosis.objects.create(reception=Rec,diagnisis=y)

                        mess = "پذیرش بیمار انجام شد." + " خدمات: " + str(L_ser).replace('[','').replace(']','').replace("'",'')
                    except:
                        alert = "پذیرش ثبت نشد ورودی ها نامعتبر هستند "
                        Rec.delete()
                else:
                    mess="ورودی ها نامعتبر هستند."
        turn = Take_Turn.objects.filter(Patient=patient)
        try:
            x =turn[turn.count()-1]
        except:
            x = None
        service = Services.objects.all()
        diagnosis = Diagnosis.objects.all()
        list_day = day_of.objects.all()
        form = ReceptionEditForm()
        today = date2jalali(D.today())
        time_now = datetime.now().strftime('%H:%M')
        return render(request, "reception/reception.html",{'form':form,'patient':patient,'turn':x,'service':service,'diagnosis':diagnosis,'now':time_now,'mess':mess,'alert':alert,'lsit_day':list_day,'today':today})
    else:
        return render(request, 'main/error.html',{'mess':'دسترسی ثبت پذیرش برای شما فعال نشده است.'})


@login_required
def recption_detail(request,id ,EntranceCode ):

    user = request.user
    x = chech_profile(user, 12)
    if x == True:
        this = get_object_or_404(Reception, id = id,EntranceCode=EntranceCode)
        if request.method == 'POST':

            if request.POST.get('state') == '1':
                price = paymentEditForm(request.POST)
                if price.is_valid():
                    this.Payable = price.cleaned_data['price']
                    this.save()
                else:
                    pass
            elif request.POST.get('state') == '2':
                payform = PayReceiptEditForm(request.POST)
                if payform.is_valid():
                    cd=payform.cleaned_data
                    pay =PaymentReceipt.objects.create(Reception=this,Device=cd['Device'],mobile =cd['mobile'], Paid=cd['Paid'])
                    pay.Cashier=request.user
                    pay.save()
                else:
                    pass
        pform =paymentEditForm()
        payform =PayReceiptEditForm()
        this_service =PatientItem.objects.filter(Reception=this)
        diagnisis =PatientDiagnosis.objects.filter(reception=this)
        paid = PaymentReceipt.objects.filter(Reception=this)
        return render(request,'reception/detail.html',{'this':this,'this_service':this_service,'pform':pform,'payform':payform,'paid':paid,'diagnisis':diagnisis})
    else:
        return render(request, 'main/error.html',{'mess':'دسترسی ثبت پذیرش برای شما فعال نشده است.'})

@login_required
def list_of_rec(request):
    user = request.user
    x = chech_profile(user, 11)
    if x == True:
        reception =Reception.objects.all()
        return render(request,'reception/rec_list.html',{'Reception':reception})
    else:
        return render(request, 'main/error.html',{'mess':'دسترسی به لیست پذیرش برای شما فعال نشده است.'})


def Refer_Surgery(request, id):
    user = request.user
    x = chech_profile(user, 14)
    if x == True:
        patient = get_object_or_404(Patient,id=id)
        if request.method == 'POST':
            surgeryform = surgeryEditForm(data=request.POST,files=request.FILES)
            if surgeryform.is_valid():
                cd= surgeryform.cleaned_data
                name =cd['name']
                Doc = cd['name_Doc']
                date = cd['date_time']
                try:
                    history =request.FILES['patient_history']
                except:
                    history = None
                try:
                    innocence =request.FILES['Medical_innocence']
                except:
                    innocence = None



                refer_to_surgery.objects.create(Patient=patient, name=name, name_Doc=Doc, date_time=date,patient_history=history, Medical_innocence=innocence)


                return redirect(patient)

        list_day = day_of.objects.all()
        form = ReceptionEditForm()
        today = date2jalali(D.today())
        form =surgeryEditForm()
        return render(request,'reception/surgery.html',{'patient':patient,'form':form,'lsit_day':list_day,'today':today} )
    else:
        return render(request, 'main/error.html',{'mess':'دسترسی ارجاع به جراحی برای اکانت شما فعال نشده است.'})
@login_required
def reToSurgery (request):

    user = request.user
    x = chech_profile(user, 14)
    if x == True:

        if request.method == 'POST':
            surgeryform = surgeryEditForm(data=request.POST, files=request.FILES)
            if surgeryform.is_valid():
                cd= surgeryform.cleaned_data
                try:
                    NationalCode = request.POST['NationalCode']
                    patient = get_object_or_404(Patient,NationalCode=NationalCode)

                    name = cd['name']
                    Doc = cd['name_Doc']
                    date = cd['date_time']
                    try:
                        history =request.FILES['patient_history']
                    except:
                        history = None
                    try:
                        innocence =request.FILES['Medical_innocence']
                    except:
                        innocence = None


                    refer_to_surgery.objects.create(Patient=patient, name=name, name_Doc=Doc, date_time=date,patient_history=history, Medical_innocence=innocence)


                    return redirect(patient)
                except:
                     return render(request, 'main/error.html',{'mess':'برای کد ملی وارد شده پرونده فعالی وجود ندارد'})
            else:
                return render(request, 'main/error.html',{'mess':'ورودی ها نامعتبر یا فاقد مقدار هستند.'})

        list_day = day_of.objects.all()
        form = ReceptionEditForm()
        today = date2jalali(D.today())
        form =refToSurgeryEditForm()
        return render(request,'reception/surgeryform.html',{'form':form,'lsit_day':list_day,'today':today} )
    else:
        return render(request, 'main/error.html',{'mess':'دسترسی ارجاع به جراحی برای اکانت شما فعال نشده است.'})
