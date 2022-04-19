from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.utils import timezone


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:

            messages.error(request, "Invalid Username/Password")
            messages.warning(request, "Please try again!!!")
            return redirect('login')
    login_form = LoginForm()
    content = {
        'login_form': login_form,
    }
    return render(request, 'pages/authenticate/login.html', content)


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('login')


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if register_form.is_valid():
            if p1 == p2:
                register_form.save()
                username = register_form.cleaned_data['username']
                password = register_form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('index')
        elif p1 != p2:
            messages.error(request, "Password doesnt match!!! Please try again")
        else:
            content = {
                'register_form': register_form,
            }
            messages.error(request, "Please try again")
            return render(request, 'pages/authenticate/register.html', content)
    register_form = RegisterForm()
    content = {
        'register_form': register_form,
    }
    return render(request, 'pages/authenticate/register.html', content)


def forgot_password(request):
    return render(request, 'pages/authenticate/forgot-password.html')


def lock_screen(request):
    return render(request, 'pages/authenticate/lock-screen.html')


@login_required(login_url='login')
def index(request):
    current_date = datetime.now().strftime("%B %d, %Y")
    app_obj = Appointment.objects.all().order_by('-date', 'time')[:5]
    appoint_obj = Appointment.objects.all()
    # return HttpResponse(date)
    doc_obj = DocProfile.objects.all()
    pat_obj = Patient.objects.all().order_by('-created_at')[:5]
    patient_obj = Patient.objects.all()

    total_apt_count = Appointment.objects.all().count()
    # today = datetime.now()
    apt_cnt = Appointment.objects.filter(created_at__month=datetime.now().month).count()
    apt_perc = apt_cnt * 100 / total_apt_count

    # New Patient %
    pat_cnt = Patient.objects.filter(created_at__month=datetime.now().month).count()
    total_pat_count = Patient.objects.all().count()
    pat_perc = pat_cnt * 100 / total_pat_count

    # Patient Under Treatment
    treatment_count = Patient.objects.filter(status='A').count()
    treatment_perc = treatment_count * 100 / total_pat_count

    discharge_count = Patient.objects.filter(status='B').count()
    discharge_perc = discharge_count * 100 / total_pat_count

    content = {
        'doc_obj': doc_obj,
        'pat_obj': pat_obj,
        'patient_obj': patient_obj,
        'app_obj': app_obj,
        'current_date': current_date,
        'opd': apt_perc,
        'new_patient': pat_perc,
        'treatment_perc': treatment_perc,
        'discharge_perc': discharge_perc,

    }
    return render(request, 'pages/index.html', content)


@login_required(login_url='login')
def my_profile(request, slug):
    doc_profile_obj = DocProfile.objects.get(slug=slug)
    content = {
        'profile_obj': doc_profile_obj,
    }
    return render(request, 'pages/doctor/profile/profile.html', content)


@login_required(login_url='login')
def edit_profile(request, slug):
    doc_edit_profile = DocProfile.objects.get(slug=slug)
    content = {
        'edit_profile': doc_edit_profile,
    }
    return render(request, 'pages/doctor/profile/edit-profile.html', content)


@login_required(login_url='login')
def settings(request):
    return render(request, 'pages/settings.html')


@login_required(login_url='login')
def doctors(request):
    doctors = DocProfile.objects.all()

    content = {
        'doc_obj': doctors,
    }
    return render(request, 'pages/doctor/doctors.html', content)


@login_required(login_url='login')
def edit_doctors(request, slug):
    edit_doc_obj = DocProfile.objects.get(slug=slug)
    all_doc = DocProfile.objects.all()
    doctor_form = DoctorForm(initial=model_to_dict(edit_doc_obj), instance=edit_doc_obj)
    country_obj = Country.objects.all()
    state_obj = State.objects.all()
    content = {
        'edit_doc': edit_doc_obj,
        'all_doc': all_doc,
        'country_obj': country_obj,
        'state_obj': state_obj,
        'doctorForm': doctor_form,
    }
    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST, request.FILES, instance=edit_doc_obj)
        if doctor_form.is_valid():
            doctor_form.save()
            messages.success(request, 'Doctor successfully Updated')
            return HttpResponseRedirect(reverse('doctors'))
    return render(request, 'pages/doctor/edit-doctor.html', content)


@login_required(login_url='login')
def add_doctor(request):
    state_obj = State.objects.all()
    country_obj = Country.objects.all()
    doctor_form = DoctorForm()

    context = {
        'state_obj': state_obj,
        'country_obj': country_obj,
        'doctorForm': doctor_form
    }
    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST, request.FILES)
        if doctor_form.is_valid():
            post = doctor_form.save(commit=False)
            post.slug = slugify(post.fname)
            post.save()
            messages.success(request, 'Doctor successfully added')
            return HttpResponseRedirect(reverse('doctors'))
        else:
            return HttpResponse(doctor_form)
    return render(request, 'pages/doctor/add-doctor.html', context)


@login_required(login_url='login')
def delete_doctors(request, slug):
    delete_doc_obj = DocProfile.objects.get(slug=slug)
    # return HttpResponse(delete_doc_obj.name)
    delete_doc_obj.delete()
    messages.success(request, 'Doctor Successfully deleted')
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def patients(request):
    pat_obj = Patient.objects.all().order_by('-updated_at')
    content = {
        'pat_obj': pat_obj
    }
    return render(request, 'pages/patient/patient.html', content)


@login_required(login_url='login')
def add_patient(request):
    country_obj = Country.objects.all()
    state_obj = State.objects.all()
    patient_form = PatientForm()
    content = {
        'country_obj': country_obj,
        'state_obj': state_obj,
        'patient_form': patient_form
    }

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        address = request.POST['address']
        country = request.POST['country']
        disease = request.POST['disease']
        state = request.POST['state']
        city = request.POST['city']
        postal_code = request.POST['postal_code']
        phone = request.POST['phone']
        image = request.FILES['image']
        status = request.POST['status']
        new_patient = Patient.objects.create(fname=fname, lname=lname, uname=uname, slug=uname, disease=disease, email=email, birthday=birthday, gender=gender, address=address, country_id=country,
                                             state_id=state,
                                             city=city,
                                             postal_code=postal_code, phone=phone, image=image, status=status)

        new_patient.save()
        messages.success(request, 'Patient successfully added')
        return HttpResponseRedirect(reverse('patients'))

    return render(request, 'pages/patient/add-patient.html', content)


@login_required(login_url='login')
def edit_patient(request, slug):
    pat_obj = Patient.objects.get(slug=slug)
    country_obj = Country.objects.all()
    state_obj = State.objects.all()
    patient_form = PatientForm(initial=model_to_dict(pat_obj), instance=pat_obj)
    context = {
        'pat_obj': pat_obj,
        'country_obj': country_obj,
        'state_obj': state_obj,
        'patient_form': patient_form,
        'pat_obj.code': pat_obj.code,
    }
    if request.method == 'POST':
        patient_form = PatientForm(request.POST, request.FILES, instance=pat_obj)
        if patient_form.is_valid():
            patient_form.save()
            messages.success(request, 'Patient successfully updated')
            return HttpResponseRedirect(reverse('patients'))
    return render(request, 'pages/patient/edit-patient.html', context)


@login_required(login_url='login')
def delete_patient(request, slug):
    pat_obj = Patient.objects.get(slug=slug)
    pat_obj.delete()
    messages.success(request, 'Successfully deleted')
    return redirect(request.META.get("HTTP_REFERER"))


@login_required(login_url='login')
def appointments(request):
    app_obj = Appointment.objects.all()
    content = {
        'app_obj': app_obj
    }
    return render(request, 'pages/appointments/appointments.html', content)


@login_required(login_url='login')
def appointment_profile(request, slug):
    appointment_obj = Appointment.objects.get(slug=slug)
    apt_form = AppointmentForm(initial=model_to_dict(appointment_obj), instance=appointment_obj)
    content = {
        'appointment_obj': appointment_obj,
        'apt_form': apt_form,
    }
    return render(request, 'pages/appointments/appointment-profile.html', content)


@login_required(login_url='login')
def add_appointment(request):
    app_obj = Appointment.objects.all()
    doc_obj = DocProfile.objects.all()
    dep_obj = Appointment.objects.all()
    country_obj = Country.objects.all()
    department_obj = Department.objects.all()
    # apt_form = AppointmentForm()
    apt_form = AppointmentForm(request.POST or None)
    content = {
        'app_obj': app_obj,
        'doc_obj': doc_obj,
        'dep_obj': dep_obj,
        'country_obj': country_obj,
        'department_obj': department_obj,
        'apt_form': apt_form,
    }
    if request.method == 'POST':
        if apt_form.is_valid():
            apt_form.save()
            messages.success(request, 'Appointment successfully added')
            return HttpResponseRedirect(reverse('appointments'))
    return render(request, 'pages/appointments/add-appointment.html', content)


@login_required(login_url='login')
def edit_appointment(request, slug):
    dep_obj = Department.objects.all()
    appointment_obj = Appointment.objects.get(slug=slug)
    doc_obj = DocProfile.objects.all()
    pat_obj = Patient.objects.all()
    apt_form = AppointmentForm(initial=model_to_dict(appointment_obj), instance=appointment_obj)
    content = {
        'doc_obj': doc_obj,
        'dep_obj': dep_obj,
        'pat_obj': pat_obj,
        'appointment_obj': appointment_obj,
        'apt_form': apt_form,
    }
    if request.method == 'POST':
        apt_form = AppointmentForm(request.POST, instance=appointment_obj)
        if apt_form.is_valid():
            apt_form.save()
            messages.success(request, 'Appointment successfully updated')
            return HttpResponseRedirect(reverse('appointments'))
    return render(request, 'pages/appointments/edit-appointment.html', content)


@login_required(login_url='login')
def delete_appointment(request, slug):
    delete_appointment_obj = Appointment.objects.get(slug=slug)
    delete_appointment_obj.delete()
    messages.success(request, 'Successfully deleted')
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def schedule(request):
    schedule_obj = Schedule.objects.all()
    content = {
        'schedule_obj': schedule_obj,
    }
    return render(request, 'pages/schedule/schedule.html', content)


@login_required(login_url='login')
def add_schedule(request):
    doct_obj = DocProfile.objects.all()
    days_obj = Days.objects.all()
    scheduleForm = ScheduleForm(request.POST or None)

    content = {
        'doct_obj': doct_obj,
        'days_obj': days_obj,
        'scheduleForm': scheduleForm,
    }
    if request.method == 'POST':
        if scheduleForm.is_valid():
            form = scheduleForm.save(commit=False)
            form.save()
            for c in request.POST.getlist('available_days'):
                form.available_days.add(c)
            messages.success(request, 'Schedule successfully created')
            return HttpResponseRedirect(reverse('schedule'))
        else:
            messages.error(request, 'Form error')
            return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'pages/schedule/add-schedule.html', content)


@login_required(login_url='login')
def edit_schedule(request, id):
    doc_obj = DocProfile.objects.all()
    schedule_obj = Schedule.objects.get(id=id)
    days_obj = Days.objects.all()
    schedule_form = ScheduleForm(initial=model_to_dict(schedule_obj), instance=schedule_obj)
    content = {
        'doc_obj': doc_obj,
        'schedule_obj': schedule_obj,
        'days_obj': days_obj,
        'schedule_form': schedule_form,
    }
    if request.method == 'POST':
        schedule_form = ScheduleForm(request.POST, instance=schedule_obj)
        if schedule_form.is_valid():
            form = schedule_form.save(commit=False)
            form.save()
            for c in request.POST.getlist('available_days'):
                form.available_days.clear()
            for c in request.POST.getlist('available_days'):
                form.available_days.add(c)
            messages.success(request, 'Schedule successfully updated')
            return HttpResponseRedirect(reverse('schedule'))
        else:

            messages.error(request, 'Form error')
            return redirect(request.META.get("HTTP_REFERER"))

    return render(request, 'pages/schedule/edit-schedule.html', content)


@login_required(login_url='login')
def delete_schedule(request, id):
    schedule_obj = Schedule.objects.get(id=id)
    schedule_obj.delete()
    messages.success(request, 'Successfully deleted')
    return redirect(request.META.get("HTTP_REFERER"))


@login_required(login_url='login')
def department(request):
    dep_obj = Department.objects.all()
    content = {
        'dep_obj': dep_obj,
    }
    return render(request, 'pages/department/department.html', content)


@login_required(login_url='login')
def add_department(request):
    dept_form = DepartmentForm()

    content = {
        'dept_form': dept_form
    }

    if request.method == 'POST':
        department = request.POST['department']
        description = request.POST['description']
        status = request.POST.get('status', False)
        for dep in Department.objects.all():
            if department == dep.department:
                messages.error(request, 'Department already exists!!!')
                messages.error(request, 'Please try to add another Department')
                return redirect(request.META.get('HTTP_REFERER', '/'))
        obj = Department.objects.create(department=department, description=description, status=status)
        obj.save()

        messages.success(request, 'Department successfully added')
        return HttpResponseRedirect(reverse('department'))
    return render(request, 'pages/department/add-department.html', content)


@login_required(login_url='login')
def edit_department(request, id):
    dept_obj = Department.objects.get(id=id)
    dept_form = DepartmentForm(initial=model_to_dict(dept_obj), instance=dept_obj)
    content = {
        'dept_obj': dept_obj,
        'dept_form': dept_form,
    }
    if request.method == 'POST':
        dept_form = DepartmentForm(request.POST, instance=dept_obj)
        if dept_form.is_valid():
            dept_form.save()
            messages.success(request, 'Department successfully updated')
            return HttpResponseRedirect(reverse('department'))
    return render(request, 'pages/department/edit-department.html', content)


@login_required(login_url='login')
def delete_department(request, id):
    dep_obj = Department.objects.get(id=id)
    dep_obj.delete()
    # messages.success(request, 'Department Successfully deleted')
    messages.success(request, f'Department \"{dep_obj.department}\" Successfully deleted')
    return redirect(request.META.get("HTTP_REFERER"))


@login_required(login_url='login')
def employee(request):
    emp_obj = Employee.objects.all()
    emp_form = EmployeeForm()

    content = {
        'emp_obj': emp_obj,
        'emp_form': emp_form,
    }
    return render(request, 'pages/employee/employee.html', content)


@login_required(login_url='login')
def delete_employee(request, slug):
    emp_obj = Employee.objects.get(slug=slug)
    emp_obj.delete()
    messages.success(request, f'Employee \"{emp_obj.fullname}\" Successfully deleted')
    return redirect(request.META.get("HTTP_REFERER"))


@login_required(login_url='login')
def add_employee(request):
    emp_obj = Employee.objects.all()
    empform = EmployeeForm()
    content = {
        'empform': empform,
        'emp_obj': emp_obj,
    }
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        age = request.POST['age']
        joining_date = request.POST['joining_date']
        phone = request.POST['phone']
        role = request.POST['role']
        status = request.POST['status']
        gender = request.POST['gender']
        image = request.FILES['image']
        new_emp = Employee.objects.create(fname=fname, lname=lname, uname=uname, slug=uname, email=email, age=age, joining_date=joining_date, phone=phone, role=role, status=status, gender=gender,
                                          image=image)
        new_emp.save()
        messages.success(request, f'Employee  Successfully added')
        return HttpResponseRedirect(reverse('employees'))
    return render(request, 'pages/employee/add-employee.html', content)


@login_required(login_url='login')
def edit_employee(request, slug):
    emp_obj = Employee.objects.get(slug=slug)
    # return HttpResponse(emp_obj)
    empform = EmployeeForm(initial=model_to_dict(emp_obj), instance=emp_obj)
    content = {
        'empform': empform,
        'emp_obj': emp_obj,
    }
    if request.method == 'POST':
        empform = EmployeeForm(request.POST, request.FILES, instance=emp_obj)
        if empform.is_valid():
            empform.save()
            messages.success(request, 'Employee successfully updated')
            return HttpResponseRedirect(reverse('employees'))
    return render(request, 'pages/employee/edit-employee.html', content)


@login_required(login_url='login')
def employee_profile(request, slug):
    emp_obj = Employee.objects.get(slug=slug)
    empform = EmployeeForm(initial=model_to_dict(emp_obj), instance=emp_obj)
    content = {
        'empform': empform,
        'emp_obj': emp_obj,
    }
    return render(request, 'pages/employee/employee-profile.html', content)


def search_employee(request):
    emp_name = request.GET['emp_name']
    emp_id = request.GET['emp_id']
    emp_role = request.GET['emp_role']

    if emp_name == '' and emp_id == '' and emp_role == 'Select Role':
        return redirect('employees')
    else:
        if emp_name == '' and emp_role == 'Select Role':
            data = Employee.objects.filter(
                Q(code__icontains=emp_id)
            )
        elif emp_id == '' and emp_role == 'Select Role':
            data = Employee.objects.filter(
                Q(fname__icontains=emp_name) |
                Q(lname__icontains=emp_name)
            )
        elif emp_name == '' and emp_id == '':
            data = Employee.objects.filter(
                Q(role__icontains=emp_role)
            )
        elif emp_id == '':
            data = Employee.objects.filter(
                (Q(fname__icontains=emp_name) |
                 Q(lname__icontains=emp_name)) &
                Q(role__icontains=emp_role)
            )
        elif emp_name == '':
            data = Employee.objects.filter(
                (Q(code__icontains=emp_id)) &
                Q(role__icontains=emp_role)
            )
        elif emp_role == 'Select Role':
            data = Employee.objects.filter(
                (Q(fname__icontains=emp_name) |
                 Q(lname__icontains=emp_name)) &
                Q(code__icontains=emp_id)
            )
        else:
            data = Employee.objects.filter(
                Q(role__icontains=emp_role) &
                (Q(fname__icontains=emp_name) |
                 Q(lname__icontains=emp_name)) &
                Q(code__icontains=emp_id)
            )
    content = {
        'date': data,
        'emp_id': emp_id,
        'emp_obj': data
    }

    return render(request, 'pages/employee/employee.html', content)

