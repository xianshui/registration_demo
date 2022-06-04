# Generated by Django 4.0.4 on 2022-06-04 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_registration', '0002_patient_delete_user_rename_user_appointment_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='time',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='password',
            field=models.CharField(max_length=16),
        ),
    ]
