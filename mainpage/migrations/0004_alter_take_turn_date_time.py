# Generated by Django 3.2.8 on 2021-10-31 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_alter_take_turn_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='take_turn',
            name='date_time',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ نوبت'),
        ),
    ]
