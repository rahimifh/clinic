from django.db import models
from django.conf import settings
class Access(models.Model):
    Service = models.CharField(max_length=100, verbose_name="نام سرویس")
    code = models.IntegerField(default= 0,verbose_name="کد سرویس")
    def __str__(self):
        return self.Service
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='profile',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True,verbose_name="نام")
    last_name = models.CharField(max_length=50,blank=True, verbose_name="نام خانوادگی")
    PersonnelCode = models.CharField(max_length=20,blank=True, null=True,verbose_name="کد پرسنلی")
    phone = models.CharField(max_length=20, default= '0', verbose_name="تلفن")
    check = models.BooleanField(default=False)
    def __str__(self):
        return f'Profile for user {self.user.username}'

# Create your models here.
class AccessItem(models.Model):
    Profile = models.ForeignKey(Profile,related_name='items',on_delete=models.CASCADE, null=True)
    Access = models.ForeignKey(Access,related_name='order_items',on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.Access)
