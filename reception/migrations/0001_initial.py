# Generated by Django 3.2.8 on 2021-11-04 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainpage', '0011_reception_payable'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Device', models.CharField(max_length=10, verbose_name='دستگاه')),
                ('mobile', models.CharField(max_length=13, verbose_name='تلفن همراه')),
                ('Paid', models.IntegerField(verbose_name='مبلغ پرداخت شده')),
                ('Cashier', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='Cashier', to=settings.AUTH_USER_MODEL, verbose_name='صندوقدار')),
                ('Reception', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Reception', to='mainpage.reception', verbose_name='پذیرش')),
            ],
            options={
                'verbose_name': 'رسید صندوق',
                'verbose_name_plural': 'رسید های صندوق',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment', models.IntegerField(verbose_name='مبلغ پرداخت شده')),
                ('PaymentId', models.CharField(blank=True, max_length=15, null=True, verbose_name='شماره پیگیری تراکنش')),
                ('Description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='توضیحات')),
                ('PaymentReceipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PaymentReceipt', to='reception.paymentreceipt', verbose_name='رسید صندوق')),
            ],
        ),
    ]
