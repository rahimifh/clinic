from django.db import models
from django.urls import reverse
from datetime import datetime, date
from jalali_date import date2jalali, datetime2jalali
from django.conf import settings
# Create your models here.
class day_of(models.Model):
    Description =models.TextField(max_length=2000, null=True, blank=True, verbose_name="توضیحات")
    date_time = models.DateField(auto_now_add=False,auto_now=False, verbose_name="تاریخ")
    def __str__(self):
        return str(self.date_time)

    class Meta:
        verbose_name = "روز تعطیل"
        verbose_name_plural = "روزهای تعطیل"
    def get_jalali_date(self):
        return date2jalali(self.date_time)

class Patient(models.Model):
    GENDER_CHOICES = ((0, 'زن'), (1, 'مرد'))
    NationalCode =  models.CharField(max_length = 10, unique=True,verbose_name="کد ملی")
    p_name = models.CharField(max_length=100,null=True, blank=True, verbose_name="نام")
    last_name = models.CharField(max_length=100,null=True, blank=True, verbose_name="نام خانوادگی")
    mobile = models.CharField(max_length=13, verbose_name="تلفن همراه")
    land_line_phone = models.CharField(max_length=13,null=True, blank=True, verbose_name="تلفن ثابت")
    age = models.IntegerField(null=True, blank=True, verbose_name="سن بیمار")
    Gender = models.IntegerField(choices=GENDER_CHOICES,null=True, blank=True, verbose_name="جنسیت")
    def __str__(self):
        return '{} {} ({})'.format(self.p_name, self.last_name, self.NationalCode)
    def get_absolute_url(self):
        if self.NationalCode != None:
            return reverse('main:patient_file', args=[self.id])
        else:
            return reverse('main:patient_file', args=[self.pk])

#------------------
class Clinic(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="نام کلینیک")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "کلینیک"
        verbose_name_plural = "کلینیک ها"
class Take_Turn(models.Model):
    part_choice = ((
        0, 'post-مغز'
        ),(
        1, 'post-کمر'
        ),(
        2,'post-هیپوفیز'
        ),(
        3, 'new-مغز'
        ),(
        4, 'new-کمر'
        ),(
        5, 'new-هیپوفیز'
        ),(
        6, 'بخیه-مغز'
        ),(
        7, 'بخیه-کمر'
        ),(
        8, 'post_گردن'
        ),(
        9, 'new_گردن'
        ))
    TURN_TYPE = ((0, 'حضوری'), (1, 'تلفنی'), (2, 'فکس'))
    Patient = models.ForeignKey('Patient', related_name='Patient1', on_delete=models.CASCADE, verbose_name="پرونده")
    TurnCode = models.CharField(max_length=10,verbose_name="کد وقت")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,related_name='turn',on_delete=models.CASCADE)
    part = models.IntegerField(choices=part_choice, verbose_name='بخش')
 #   Day = models.IntegerField(choices=WEEK_DAY, verbose_name="روز")
    #clinic = models.ForeignKey('Clinic', related_name='clinic', on_delete=models.CASCADE, verbose_name="کلینیک")
    date = models.DateTimeField(auto_now=True,verbose_name="تاریخ ثبت نوبت")
    date_time = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True, verbose_name="(2021-01-01)تاریخ نوبت")
    TypeTurn = models.IntegerField(choices=TURN_TYPE, null=True, blank=True, verbose_name="نوع در خواست وقت")
    Description =models.TextField(max_length=2000, null=True, blank=True, verbose_name="توضیحات")
    def __str__(self):
        return str(self.Patient)

    class Meta:
        verbose_name = "نوبت"
        verbose_name_plural = "نوبت ها"
    def get_jalali_date(self):
        return datetime2jalali(self.date_time)


#پذیرش
class Services(models.Model):
    Service = models.CharField(max_length=100, verbose_name="نام خدمت")
    Price = models.DecimalField(max_digits=10, decimal_places=2,default= 0)

    def __str__(self):
        return self.Service
    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمت های قابل ارائه"
class Diagnosis(models.Model):
    D_name = models.CharField(max_length=200, verbose_name="نام خدمت")
    def __str__(self):
        return self.D_name
    class Meta:
        verbose_name = "تشخیص"
        verbose_name_plural = "تشخیص"

# Create your models here.
class Reception (models.Model):
    LEVEL = ((0, 'جدید'), (1, 'بعد از عمل'), (2,'رویت MRA'))

    Patient = models.ForeignKey('Patient', related_name='Patient2', on_delete=models.CASCADE, verbose_name="پرونده")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,related_name='reception',on_delete=models.CASCADE)
    TypeTurn = models.IntegerField(choices=LEVEL, default=0, verbose_name="مرحله")
    #Receptionist = models.ForeignKey('Receptionist', related_name='Receptionist', on_delete=models.SET_NULL,verbose_name="مسئول پذیرش")

    EntranceCode = models.IntegerField(verbose_name="کد پذیرش")
    TurnCode = models.CharField(max_length=10,verbose_name="کد وقت")
    EntranceDate = models.DateTimeField(auto_now=True,verbose_name="تاریخ پذیرش")
    date = models.DateTimeField(verbose_name="تاریخ نوبت")
    Referrer = models.CharField(max_length=100,null=True, blank=True, verbose_name="معرف")
    Description =models.TextField(max_length=2000, null=True, blank=True, verbose_name="توضیحات")
    Payable = models.IntegerField(verbose_name="قابل پرداخت",default=0)
    def __str__(self):
                return str(self.Patient)

    class Meta:
        verbose_name = "بیمار"
        verbose_name_plural = "بیماران پذیرش شده"
    def get_absolute_url(self):
        return reverse('reception:receptionDetaile',args=[self.id, self.EntranceCode])
    def get_jalali_date(self):
        return datetime2jalali(self.EntranceDate)
class PatientItem(models.Model):
    Reception = models.ForeignKey(Reception,related_name='items',on_delete=models.CASCADE, null=True)
    Services = models.ForeignKey(Services,related_name='order_items',on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.Services)
    def get_cost(self):
        return self.price * self.quantity

class PatientDiagnosis(models.Model):
    reception = models.ForeignKey(Reception,related_name='diagnisisReception',on_delete=models.CASCADE, null=True)
    diagnisis = models.ForeignKey(Diagnosis,related_name='diagnisis',on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.diagnisis)


#**********
