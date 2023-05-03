from django.contrib import admin
from .models import PaymentReceipt,refer_to_surgery
from django.db import models
from django.forms import Textarea
# Register your models here.
@admin.register(PaymentReceipt)
class PaymentReceiptAdmin(admin.ModelAdmin):
    list_display = ['Reception','Cashier']
    #list_filter = ['Receptionist',]
    search_fields = ['Reception','Cashier']
@admin.register(refer_to_surgery)
class PaymentReceiptAdmin(admin.ModelAdmin):
    list_display = ['Patient','name','name_Doc']
    #list_filter = ['Receptionist',]
    search_fields = ['Reception','Cashier']
