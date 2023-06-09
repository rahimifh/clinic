# Generated by Django 3.2.8 on 2021-10-31 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EntranceCode', models.IntegerField(verbose_name='کد پذیرش')),
                ('p_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('age', models.IntegerField(verbose_name='سن بیمار')),
                ('NationalCode', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('Device', models.CharField(max_length=10, verbose_name='دستگاه')),
                ('Receptionist', models.CharField(max_length=100, verbose_name='مسئول پذیرش')),
                ('mobile', models.CharField(max_length=13, verbose_name='تلفن همراه')),
                ('Payable', models.IntegerField(verbose_name='قابل پرداخت')),
                ('Payment', models.IntegerField(verbose_name='مانده')),
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
                ('EntranceCode', models.IntegerField(verbose_name='کد پذیرش')),
                ('NationalCode', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('PaymentId', models.CharField(blank=True, max_length=15, null=True, verbose_name='شماره پیگیری تراکنش')),
                ('Description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='توضیحات')),
                ('Cashier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PaymentReceipt', to='cash_desk.paymentreceipt', verbose_name='رسید صندوق')),
            ],
        ),
    ]
