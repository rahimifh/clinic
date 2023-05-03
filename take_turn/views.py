from django.shortcuts import render, redirect, get_object_or_404
from .forms import TakeTurnEditForm,TakeTurnEditForm_S
from mainpage.models import Take_Turn,Patient,day_of
from django.contrib.auth.models import User
import pytz
import time
from datetime import datetime, timedelta,date
from jalali_date import date2jalali
from account.check_user import chech_profile
# Create your views here.
def take_turn(request):
    user = request.user
    x = chech_profile(user, 10)
    if x == True:
        all_t = Take_Turn.objects.order_by('-date_time')
        all_turns = []
        tz = pytz.timezone('Asia/Tehran')
        for i in all_t:
            if tz.localize(datetime.now())> i.date_time:
                all_turns.append(i)
            else:
                all_turns.append(i)
        if request.method == 'POST':
            turn_form = TakeTurnEditForm(request.POST)
            if turn_form.is_valid():
                AllPatient =Patient.objects.all()
                cd =turn_form.cleaned_data
                part1 = cd['part']
                d = cd['date_time']
                count = 1
                for i in all_turns:
                    d1 = i.date_time
                    if d1.date() == d.date() and part1 == i.part:
                        count += 1
                partlist = ['PM-','PK-','PH-','NM-','NK-','PH-','BM-','BK-','PG-','NG-']
                turncode = partlist[part1] + str(count)
                patient1 = cd['Patient']
                for patient in AllPatient:
                    if patient.NationalCode == patient1:
                        P =Patient.objects.get(NationalCode=patient1)
                        Take_Turn.objects.create(Patient=P,TurnCode = turncode,user=user,part=cd['part'],date_time=cd['date_time'],TypeTurn=cd['TypeTurn'],Description=cd['Description'])
                        
                        return redirect('turn:take_turn')
                Npationt=Patient.objects.create(NationalCode=cd['Patient'],mobile=cd['mobile'],p_name=cd['First_name'],last_name=cd['Last_name'])
                Take_Turn.objects.create(Patient=Npationt ,TurnCode=turncode,user=user,part=cd['part'],date_time=cd['date_time'],TypeTurn=cd['TypeTurn'],Description=cd['Description'])
                form = TakeTurnEditForm()
                return redirect('main:home')
            else:
                pass

        all_turns = Take_Turn.objects.order_by('-date_time')
        form = TakeTurnEditForm()
        list_day = day_of.objects.all()
        today = date2jalali(date.today())

        return render(request,"turn/turn.html",{'form': form,'turn':all_turns,'lsit_day':list_day,'today':today})
    else:
        return render(request, 'main/error.html',{'mess':'دسترسی ثبت نوبت برای شما فعال نشده است.'})

def take_turn_s(request, id):
    user = request.user
    x = chech_profile(user, 10)
    if x == True:
        mess =None
        all_t = Take_Turn.objects.order_by('-date_time')
        all_turns = []
        tz = pytz.timezone('Asia/Tehran')
        for i in all_t:
            if tz.localize(datetime.now())> i.date_time:
                all_turns.append(i)
            else:
                all_turns.append(i)
        if request.method == 'POST':
            print(id)
            turn_form = TakeTurnEditForm_S(request.POST)
            if turn_form.is_valid():
                AllPatient =Patient.objects.all()
                cd =turn_form.cleaned_data
                P =get_object_or_404(Patient,id=id)
                part1 = cd['part']
                d = cd['date_time']
                count = 1
                for i in all_turns:
                    d1 = i.date_time
                    if d1.date() == d.date() and part1 == i.part:
                        count += 1
                partlist = ['PM-','PK-','PH-','NM-','NK-','PH-','BM-','BK-','PG-','NG-']
                turncode = partlist[part1] + str(count)
                Take_Turn.objects.create(Patient=P,TurnCode=turncode,user=user,part=cd['part'],date_time=cd['date_time'],TypeTurn=cd['TypeTurn'],Description=cd['Description'])
                #form = TakeTurnEditForm_S()
                #patient = get_object_or_404(Patient,NationalCode=NationalCode)
                #return render(request,"turn/turn.html",{'form': form,'mess':"وقت براي بيمار رزرو شد.","patient":patient})
                mess = "وقت براي بيمار رزرو شد."

        #all_turns = Take_Turn.objects.order_by('-date_time')
        patient = get_object_or_404(Patient,id=id)
        form =TakeTurnEditForm_S()
        list_day = day_of.objects.all()
        today = date2jalali(date.today())

        return render(request,"turn/turn.html",{'form': form,"patient":patient,'mess':mess,'turn':all_turns,'lsit_day':list_day,'today':today})
    else:
        return render(request, 'main/error.html',{'mess':'دسترسی ثبت نوبت برای شما فعال نشده است.'})


def delete_turn(request, id):
    if request.method == 'POST':
        turn  =get_object_or_404(Take_Turn,id=id)
        turn.delete()
        return redirect('turn:take_turn')

def delete_turn_h(request, id):
    if request.method == 'POST':
        turn  =get_object_or_404(Take_Turn,id=id)
        turn.delete()
        return redirect('main:home')
    else:
        turn  =get_object_or_404(Take_Turn,id=id)
        pationt =turn.Patient
        turn.delete()

        return redirect(pationt)
