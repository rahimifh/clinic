# Generated by Django 3.2.8 on 2021-11-04 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_auto_20211101_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reception',
            name='FileNumber',
        ),
    ]
