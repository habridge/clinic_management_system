# Generated by Django 4.0.3 on 2022-03-17 06:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import myclinic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('United States', 'United States'), ('United Kingdom', 'United Kingdom'), ('Australia', 'Australia'), ('Nepal', 'Nepal'), ('China', 'China'), ('Poland', 'Poland'), ('Japan', 'Japan')], max_length=25, verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'Country',
            },
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Days',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('DEN', 'Dentists'), ('NEU', 'Neurology'), ('OPT', 'Opthamology'), ('ORT', 'Orthopedics'), ('CAN', 'Cancer Department'), ('ENT', 'ENT Department')], max_length=93)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('A', 'Active'), ('B', 'Inactive')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Departmentzz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=93)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('A', 'Active'), ('B', 'Inactive')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='DocProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postal_code', models.IntegerField()),
                ('medical_area', models.CharField(max_length=255)),
                ('emp_id', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='img')),
                ('edu_info', models.TextField(blank=True, max_length=250, validators=[django.core.validators.MaxLengthValidator(250)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('status', models.CharField(choices=[('A', 'Active'), ('B', 'Inactive')], max_length=1)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='countryz', to='myclinic.country')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=myclinic.models.generate_id_length, editable=False, max_length=7, unique=True)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('uname', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='img/Employee')),
                ('email', models.EmailField(max_length=255)),
                ('joining_date', models.DateField()),
                ('phone', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Doctor', 'Doctor'), ('Nurse', 'Nurse'), ('Laboratorist', 'Laboratorist'), ('Pharmacist', 'Pharmacist'), ('Accountant', 'Accountant'), ('Receptionist', 'Receptionist')], max_length=15)),
                ('status', models.CharField(choices=[('A', 'Active'), ('B', 'Inactive')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Province 1', 'Province 1'), ('Madhesh Province', 'Madhesh Province'), ('Bagmati Province', 'Bagmati Province'), ('Gandaki Province', 'Gandaki Province'), ('Lumbini Province', 'Lumbini Province'), ('Karnali Province', 'Karnali Province'), ('Sudurpashim Province', 'Sudurpashim Province')], max_length=25)),
            ],
            options={
                'verbose_name_plural': 'State',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('B', 'Inactive')], default='Active', max_length=1)),
                ('available_days', models.ManyToManyField(to='myclinic.days')),
                ('dep_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myclinic.department', verbose_name='Department')),
                ('doc_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myclinic.docprofile', verbose_name='Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('uname', models.CharField(max_length=255, verbose_name='username')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=255)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postal_code', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='img/patients')),
                ('status', models.CharField(choices=[('A', 'Active'), ('B', 'Inactive')], max_length=1)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myclinic.country')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myclinic.state')),
            ],
        ),
        migrations.AddField(
            model_name='docprofile',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myclinic.state'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(editable=False, max_length=7, unique=True, verbose_name='Appointment')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.IntegerField()),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('A', 'Active'), ('B', 'Inactive')], max_length=1)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myclinic.country')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myclinic.department')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myclinic.docprofile')),
            ],
        ),
    ]