# Generated by Django 4.0.3 on 2022-03-18 03:25

from django.db import migrations, models
import django.db.models.deletion
import myclinic.models


class Migration(migrations.Migration):

    dependencies = [
        ('myclinic', '0012_alter_appointment_code_alter_docprofile_code_and_more'),
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
            model_name='docprofile',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countryz', to='myclinic.country'),
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
