# Generated by Django 4.0.3 on 2022-03-22 12:40

from django.db import migrations, models
import myclinic.models


class Migration(migrations.Migration):

    dependencies = [
        ('myclinic', '0028_employee_alter_appointment_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='code',
            field=models.CharField(default=myclinic.models.generate_id_length, editable=False, max_length=7, unique=True, verbose_name='Appointment ID'),
        ),
        migrations.AlterField(
            model_name='docprofile',
            name='code',
            field=models.CharField(default=myclinic.models.generate_id_length, editable=False, max_length=7, unique=True, verbose_name='Doctor ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='code',
            field=models.CharField(default=myclinic.models.generate_id_length, editable=False, max_length=7, unique=True, verbose_name='Patient ID'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='code',
            field=models.CharField(default=myclinic.models.generate_id_length, editable=False, max_length=7, unique=True, verbose_name='Schedule ID'),
        ),
    ]