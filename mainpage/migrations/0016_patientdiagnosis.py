# Generated by Django 3.2.8 on 2021-11-14 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0015_diagnosis'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDiagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnisis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diagnisis', to='mainpage.diagnosis')),
                ('reception', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diagnisisReception', to='mainpage.reception')),
            ],
        ),
    ]