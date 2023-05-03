from django.contrib import admin
from .models import PaymentReceipt,Payment
from django.db import models
from django.forms import Textarea
# Register your models here.
@admin.register(PaymentReceipt)
class PaymentReceiptAdmin(admin.ModelAdmin):
    list_display = ['EntranceCode', 'p_name', 'last_name','NationalCode' ]
    #list_filter = ['Receptionist',]
    search_fields = ['NationalCode','p_name', 'last_name','EntranceCode']
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['EntranceCode','NationalCode' ]
    #list_filter = ['Receptionist',]
    search_fields = ['NationalCode','EntranceCode']
    formfield_overrides = {
                models.TextField: {'widget': Textarea(
                                   attrs={
                                          'style': 'direction: rtl;'})},
            }
