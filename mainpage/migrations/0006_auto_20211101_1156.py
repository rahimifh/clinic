# Generated by Django 3.2.8 on 2021-11-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_alter_take_turn_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='take_turn',
            name='FileNumber',
        ),
        migrations.AlterField(
            model_name='take_turn',
            name='date_time',
            field=models.DateTimeField(blank=True, verbose_name='(2021-01-01)تاریخ نوبت'),
        ),
    ]
