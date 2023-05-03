from django.db import models
from mainpage.models import Reception,Patient
from django.contrib.auth.models import User
from jalali_date import date2jalali
# Create your models here.

class PaymentReceipt(models.Model):
    Reception=models.ForeignKey(Reception, related_name='paymentReception', on_delete=models.CASCADE,verbose_name='پذیرش')
    Device = models.CharField(max_length = 10,verbose_name="دستگاه")
    Cashier = models.ForeignKey(User,related_name='Cashier', on_delete=models.CASCADE,default= '1', verbose_name="صندوقدار")
    mobile = models.CharField(max_length=13, verbose_name="تلفن همراه")
    Paid = models.IntegerField(verbose_name="مبلغ پرداخت شده")
    def __str__(self):
        return '{} {}'.format(self.Cashier, self.Reception)

    class Meta:
        verbose_name = "رسید صندوق"
        verbose_name_plural = "رسید های صندوق"

class refer_to_surgery(models.Model):
    Patient=models.ForeignKey(Patient, related_name='surgerypatuent', on_delete=models.CASCADE,verbose_name='بيمار')
    date_time = models.DateField(auto_now_add=False,auto_now=False, verbose_name="تاریخ")
    name = models.CharField(max_length = 200,verbose_name="عنوان عمل جراحي")
    name_Doc = models.CharField(max_length = 50,verbose_name="نام پزشك معالج")
    patient_history = models.FileField(upload_to='patient_history/%Y/%m/%d', null=True, blank=True,verbose_name='شرح حال')
    Medical_innocence= models.FileField(upload_to='Medical_innocence/%Y/%m/%d', null=True, blank=True,verbose_name='برائت نامه')
    def __str__(self):
        return '{}- Doctor:{}'.format(self.Patient, self.name_Doc)
    class Meta:
        verbose_name = "ارجاع به جراحي"
        verbose_name_plural = "ارجاع ها به جراحي"
    def get_jalali_date(self):
        return date2jalali(self.date_time)
