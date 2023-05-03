from django.contrib import admin
from .models import Patient, Clinic,Take_Turn,Services,Reception,PatientItem,day_of,Diagnosis,PatientDiagnosis
from django.db import models
from django.forms import Textarea
# Register your models here.
@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
        list_display = ['D_name' ]
@admin.register(day_of)
class TakeTurnAdmin(admin.ModelAdmin):
    list_display = ['Description','date_time' ]
    list_filter = ['date_time']
    formfield_overrides = {
            models.TextField: {'widget': Textarea(
                               attrs={
                                      'style': 'direction: rtl;'})},
        }
class ServicesItemInline(admin.TabularInline):
    model = PatientItem
    raw_id_fields = ['Reception']

class DiagnosisInline(admin.TabularInline):
    model = PatientDiagnosis
    raw_id_fields = ['reception']
@admin.register(Patient)
class patientAdmin(admin.ModelAdmin):
    list_display = ['NationalCode','p_name','last_name','mobile','Gender' ]
    list_filter = ['Gender','age']
    search_fields = ['NationalCode','mobile']

@admin.register(Clinic)
class linicAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(Take_Turn)
class TakeTurnAdmin(admin.ModelAdmin):
    list_display = ['Patient','date','date_time','TurnCode' ]
    list_filter = ['TypeTurn']
    search_fields = ['Patient', 'date']
    formfield_overrides = {
            models.TextField: {'widget': Textarea(
                               attrs={
                                      'style': 'direction: rtl;'})},
        }


@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    list_display = ['Patient', 'EntranceCode', 'TurnCode','date' ]
    #list_filter = ['Receptionist',]
    inlines = [ServicesItemInline,DiagnosisInline]
    search_fields = ['Patient','EntranceCode', 'TurnCode']
    formfield_overrides = {
            models.TextField: {'widget': Textarea(
                               attrs={
                                      'style': 'direction: rtl;'})},
        }
@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','Service', 'Price']
    search_fields = ['Service']
