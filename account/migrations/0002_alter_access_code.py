# Generated by Django 3.2.8 on 2021-11-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='code',
            field=models.IntegerField(default=0, verbose_name='کد سرویس'),
        ),
    ]
