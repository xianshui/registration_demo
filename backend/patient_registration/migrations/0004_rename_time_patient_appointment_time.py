# Generated by Django 4.0.4 on 2022-06-04 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_registration', '0003_patient_time_alter_patient_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='time',
            new_name='appointment_time',
        ),
    ]