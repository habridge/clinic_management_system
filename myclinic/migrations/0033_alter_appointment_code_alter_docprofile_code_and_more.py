# Generated by Django 4.0.3 on 2022-04-06 13:10

from django.db import migrations, models
import django.db.models.deletion
import myclinic.models


class Migration(migrations.Migration):

    dependencies = [
        ('myclinic', '0032_alter_appointment_code_alter_docprofile_code_and_more'),
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
            model_name='patient',
            name='code',
            field=models.CharField(default=myclinic.models.generate_id_length, editable=False, max_length=7, unique=True, verbose_name='Patient ID'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='code',
            field=models.CharField(default=myclinic.models.generate_id_length, editable=False, max_length=7, unique=True, verbose_name='Schedule ID'),
        ),
        migrations.CreateModel(
            name='EmpLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('Medical Leave', 'Medical Leave'), ('Casual Leave 12 Days', 'Casual Leave Type'), ('Loss of Pay', 'Loss of Pay')], max_length=25)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('reason', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('N', 'New'), ('A', 'Approved'), ('D', 'Declined')], max_length=1)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myclinic.employee')),
            ],
            options={
                'verbose_name_plural': 'Employee Leave',
            },
        ),
    ]