# Generated by Django 3.2.8 on 2021-11-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_alter_patient_nationalcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reception',
            name='EntranceDate',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ پذیرش'),
        ),
    ]
