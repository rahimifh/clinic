# Generated by Django 3.2 on 2021-11-01 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_alter_take_turn_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='take_turn',
            name='date_time',
            field=models.DateTimeField(blank=True, verbose_name='تاریخ نوبت'),
        ),
    ]
