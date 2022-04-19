from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

from .models import *
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    password = fields.CharField(widget=forms.PasswordInput)

    # username = fields.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None,
        }


class RegisterForm(UserCreationForm):
    username = forms.CharField(help_text=False)

    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    terms = forms.BooleanField(
        # error_messages={'required': 'Please let us know what to call you!'},
        label="Terms & Conditions",
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'phone', 'terms']
        # help_texts = {
        #     'username': None,
        # }


class ScheduleForm(forms.ModelForm):
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=Schedule.STATE_CHOICES, initial='A')

    class Meta:
        model = Schedule

        # available_days = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=Days.DAYS_CHOICES)
        available_days = forms.ModelMultipleChoiceField(queryset=Days.objects.all(), widget=forms.SelectMultiple)

        # fields = ['doc_obj','dep_obj', 'available_days', 'start_time', 'end_time', 'message', 'status']
        fields = '__all__'

        widgets = {
            # 'doc_obj': forms.Select(attrs={'class': 'form-group select', 'placeholder': 'Select'}),
            'available_days': forms.SelectMultiple(attrs={'class': 'form-group select'}),
            # 'company': Select2MultipleWidget(),
            # 'status': forms.Select(attrs={'class': 'form-check form-check-inline','display': 'inline-flex'}),
            'status': forms.RadioSelect(attrs={'class': 'form-check form-check-inline '}),
            'start_time': forms.DateTimeInput(attrs={'class': 'timez'}),
            'end_time': forms.DateTimeInput(attrs={'class': 'timez'}),
            # widget = forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}),
        }


class DepartmentForm(forms.ModelForm):
    model = Departmentzz
    # STATE_CHOICES = {
    #     ('A', 'Active'),
    #     ('I', 'Inactive'),
    # }
    # status = forms.ChoiceField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=STATE_CHOICES))
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=Department.STATE_CHOICES)

    class Meta:
        model = Department
        fields = ['department', 'description', 'status']

    # field_order = ['department', ]


class DoctorForm(forms.ModelForm):
    # model = DocProfile
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=DocProfile.GENDER_CHOICES)
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=DocProfile.STATE_CHOICES)
    slug = forms.SlugField(required=False)
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = DocProfile
        fields = '__all__'

        labels = {
            'edu_info': "Short Biography",
            'fname': 'First Name',
            'lname': 'Last Name',
            'birthday': 'Date of Birth'
        }
        widgets = {
            # 'gender': forms.RadioSelect(attrs={'class': 'form-check form-check-inline'})
            # 'image': forms.Select(attrs={'padding':'0'})
            'status': forms.RadioSelect(attrs={'display': 'inline-flex'}),
            'edu_info': forms.Textarea(attrs={'rows': 3, 'cols': 15}),
            'medical_area': forms.Textarea(attrs={'rows': 3, 'cols': 15}),
            # 'birthday': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'birthday': forms.DateTimeInput(attrs={'class': 'datetime-input cal-icon'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["slug"].disabled = True
        # Or to set READONLY
        self.fields["slug"].widget.attrs["readonly"] = True


class PatientForm(forms.ModelForm):
    # birthday=forms.DateTimeField(widget=forms.DateTimeField())
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=Patient.STATE_CHOICES)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=Patient.GENDER_CHOICES)
    image = forms.ImageField(widget=forms.FileInput)
    slug = forms.SlugField(required=False)

    class Meta:
        model = Patient

        fields = '__all__'
        # fields=['fname','lname','uname','email','birthday','gender','address','country','state','city','postal_code','phone','image','status']
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'birthday': 'Date of Birth'
        }

        widgets = {
            # 'birthday':forms.DateField(attrs={'class':'datetimepicker'})
            'birthday': forms.DateTimeInput(attrs={'class': 'datetime-input cal-icon'}),
            'status': forms.RadioSelect(attrs={'class': 'ranjan'}),
            'gender': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["slug"].disabled = True
        # Or to set READONLY
        self.fields["slug"].widget.attrs["readonly"] = True


class AppointmentForm(forms.ModelForm):
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=Patient.STATE_CHOICES)
    slug = forms.SlugField(required=False)

    class Meta:
        model = Appointment
        fields = '__all__'
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
        }

        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'time': forms.DateTimeInput(attrs={'class': 'time-input'}),
            'message': forms.Textarea(attrs={'rows': 3, 'cols': 15}),
            'status': forms.RadioSelect(attrs={'class': 'form-check-inline'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["slug"].disabled = True
        # Or to set READONLY
        self.fields["slug"].widget.attrs["readonly"] = True


class EmployeeForm(forms.ModelForm):
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=Employee.STATE_CHOICES)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=Employee.GENDER_CHOICES)
    slug = forms.SlugField(required=False)
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['fname', 'lname', 'uname', 'email', 'age', 'joining_date', 'role', 'phone', 'image', 'status', 'gender']

        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'uname': 'UserName',
            'age': 'Date of Birth'
        }

        widgets = {
            'age': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'joining_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["slug"].disabled = True
        # Or to set READONLY
        self.fields["slug"].widget.attrs["readonly"] = True


class LeaveForm(forms.ModelForm):
    # no_of_days = forms.DateTimeField(widget=forms.DateTimeField)
    # no_of_days = forms.DateTimeField(widget=forms.Select(attrs={'onchange': "cal();"}))
    # to_date = forms.DateTimeField(input_formats=['%m/%d/%Y'])
    # to_date = forms.DateTimeField(input_formats=['%m/%d/%Y'])

    class Meta:
        model = EmpLeave
        fields = '__all__'

        widgets = {
            'reason': forms.Textarea(attrs={'rows': 3, 'cols': 15}),
            'from_date': forms.DateTimeInput(attrs={'onchange': 'cal()', 'class': 'datetime-input'}),
            'to_date': forms.DateTimeInput(attrs={'onchange': 'cal()', 'class': 'datetime-input'}),
            # 'to_date': forms.DateTimeInput( forms.Select(attrs={'onchange': 'cal()'})),
            # 'to_date': forms.DateTimeInput(forms.Select(attrs={'onchange': 'cal()';}))

        }
