from django.db import models

# Create your models here.
'''
class Cashier(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="نام کلینیک")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "صندوق دار"
        verbose_name_plural = "صندوق دارها"
'''
class PaymentReceipt(models.Model):

    #Cashier=models.ForeignKey('Cashier', related_name='Cashier', on_delete=models.SET_NULL,verbose_name="صندوق دار")
    EntranceCode = models.IntegerField(verbose_name="کد پذیرش")
    p_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    age = models.IntegerField(verbose_name="سن بیمار")
    NationalCode =  models.CharField(max_length = 10,verbose_name="کد ملی")
    Device = models.CharField(max_length = 10,verbose_name="دستگاه")
    Receptionist = models.CharField(max_length=100, verbose_name="مسئول پذیرش")
    mobile = models.CharField(max_length=13, verbose_name="تلفن همراه")
    Payable = models.IntegerField(verbose_name="قابل پرداخت")
    Payment = models.IntegerField(verbose_name="مانده")
    def __str__(self):
        return '{} {} ({})'.format(self.p_name, self.last_name, self.EntranceCode)

    class Meta:
        verbose_name = "رسید صندوق"
        verbose_name_plural = "رسید های صندوق"

class Payment(models.Model):
    EntranceCode = models.IntegerField(verbose_name="کد پذیرش")
    NationalCode =  models.CharField(max_length = 10,verbose_name= "کد ملی")
    PaymentId = models.CharField(max_length=15, null=True, blank=True, verbose_name="شماره پیگیری تراکنش")
    Description =models.TextField(max_length=2000, null=True, blank=True, verbose_name="توضیحات")
    Cashier=models.ForeignKey('PaymentReceipt', related_name='PaymentReceipt', on_delete=models.CASCADE,verbose_name="رسید صندوق")
