# Generated by Django 3.2.8 on 2021-10-31 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service', models.CharField(max_length=100, verbose_name='نام سرویس')),
                ('code', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='کد سرویس')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='نام خانوادگی')),
                ('PersonnelCode', models.CharField(blank=True, max_length=20, null=True, verbose_name='کد پرسنلی')),
                ('phone', models.CharField(default='0', max_length=20, verbose_name='تلفن')),
                ('check', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccessItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Access', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='account.access')),
                ('Profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='account.profile')),
            ],
        ),
    ]
