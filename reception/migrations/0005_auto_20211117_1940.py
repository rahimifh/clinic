# Generated by Django 3.2.8 on 2021-11-17 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0017_alter_reception_referrer'),
        ('reception', '0004_refer_to_surgery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='refer_to_surgery',
            options={'verbose_name': 'ارجاع به جراحي', 'verbose_name_plural': 'ارجاع ها به جراحي'},
        ),
        migrations.AlterField(
            model_name='refer_to_surgery',
            name='Medical_innocence',
            field=models.FileField(upload_to='Medical_innocence/%Y/%m/%d', verbose_name='برائت نامه'),
        ),
        migrations.AlterField(
            model_name='refer_to_surgery',
            name='Patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surgerypatuent', to='mainpage.patient', verbose_name='بيمار'),
        ),
        migrations.AlterField(
            model_name='refer_to_surgery',
            name='patient_history',
            field=models.FileField(upload_to='patient_history/%Y/%m/%d', verbose_name='شرح حال'),
        ),
    ]
