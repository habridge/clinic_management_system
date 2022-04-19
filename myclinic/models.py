# from django import forms
from django import forms
from django.conf import settings
from django.core import serializers
from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models import TimeField
from django.utils.crypto import get_random_string
from datetime import datetime

# Create your models here.`
from django.utils.text import slugify
import random
import string
from .slug import unique_slugify


# '''
# random_string_generator is located here:
# http://joincfe.com/blog/random-string-generator-in-python/
# '''


# from clinic_management_system.utils import random_string_generator
# from utils import random_string_generator


# def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
#     # print(''.join(random.choice(chars) for _ in range(size)))
#     return ''.join(random.choice(chars) for _ in range(size))

# def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))


# def unique_slug_generator(instance, new_slug=None):
#     """
#     This is for a Django project and it assumes your instance
#     has a model with a slug field and a title character (char) field.
#     """
#
#     if new_slug is not None:
#         slug = new_slug
#     else:
#         slug = slugify(instance.fname)
#
#     Klass = instance.__class__
#     qs_exists = Klass.objects.filter(slug=slug).exists()
#     if qs_exists:
#         new_slug = "{slug}-{randstr}".format(
#             slug=slug,
#             randstr=random_string_generator(size=4)
#             # randstr=random_string_generator(7).upper()
#         )
#         # print(unique_slug_generator(instance, new_slug=new_slug))
#         return unique_slug_generator(instance, new_slug=new_slug)
#     return slug


def generate_id_length():
    code_length = 7
    return get_random_string(code_length).upper()


class Country(models.Model):
    COUNTRY_CHOICES = (
        ('United States', 'United States'),
        ('United Kingdom', 'United Kingdom'),
        ('Australia', 'Australia'),
        ('Nepal', 'Nepal'),
        ('China', 'China'),
        ('Poland', 'Poland'),
        ('Japan', 'Japan'),
    )
    country = models.CharField(max_length=25, choices=COUNTRY_CHOICES, verbose_name="Country")

    class Meta:
        verbose_name_plural = "Country"

    def __str__(self):
        return self.country


class State(models.Model):
    STATE_CHOICES = (
        ('Province 1', 'Province 1'),
        ('Madhesh Province', 'Madhesh Province'),
        ('Bagmati Province', 'Bagmati Province'),
        ('Gandaki Province', 'Gandaki Province'),
        ('Lumbini Province', 'Lumbini Province'),
        ('Karnali Province', 'Karnali Province'),
        ('Sudurpashim Province', 'Sudurpashim Province'),
    )
    state = models.CharField(max_length=25, choices=STATE_CHOICES)

    class Meta:
        verbose_name_plural = "State"

    def __str__(self):
        return self.state


class Department(models.Model):
    DEPARTMENT_CHOICES = (
        ('Dentists', 'Dentists'),
        ('Neurology', 'Neurology'),
        ('Opthamology', 'Opthamology'),
        ('Orthopedics', 'Orthopedics'),
        ('Cancer Department', 'Cancer Department'),
        ('ENT Department', 'ENT Department'),
    )
    # DEPARTMENT_CHOICES = (
    #     ('DEN', 'Dentists'),
    #     ('NEU', 'Neurology'),
    #     ('OPT', 'Opthamology'),
    #     ('ORT', 'Orthopedics'),
    #     ('CAN', 'Cancer Department'),
    #     ('ENT', 'ENT Department'),
    # )
    department = models.CharField(max_length=93, choices=DEPARTMENT_CHOICES)
    description = models.TextField()

    STATE_CHOICES = (
        ('A', 'Active'),
        ('B', 'Inactive'),
    )
    status = models.CharField(max_length=1, choices=STATE_CHOICES)

    def is_activated(self):
        if self.status == 'A':
            return True
        return False

    is_activated.boolean = True
    is_activated.short_description = "Status"

    def __str__(self):
        return self.department


class Departmentzz(models.Model):
    department = models.CharField(max_length=93)
    description = models.TextField()

    STATE_CHOICES = (
        ('A', 'Active'),
        ('B', 'Inactive'),
    )
    status = models.CharField(max_length=1, choices=STATE_CHOICES)

    def is_activated(self):
        if self.status == 'A':
            return True
        return False

    is_activated.boolean = True
    is_activated.short_description = "Status"

    def __str__(self):
        return self.department


class Days(models.Model):
    DAYS_CHOICES = (
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )
    # days = models.CharField(max_length=10, choices=DAYS_CHOICES)
    days = models.CharField(max_length=10, choices=DAYS_CHOICES)

    class Meta:
        verbose_name_plural = 'Days'

    def __str__(self):
        return self.days

    # def dayz(self):
    #     return ("%s" % (self.days   ))
    #
    # dayz.short_description = 'Choose days'


class DocProfile(models.Model):
    code_length = 7
    code = models.CharField(max_length=code_length, editable=False, default=generate_id_length, unique=True, verbose_name='Doctor ID')
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, **kwargs):
        slug = '%s' % self.fname
        unique_slugify(self, slug)
        super(DocProfile, self).save()

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    username = models.CharField(max_length=255)

    # country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True, related_name='countryz')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True, related_name='countryz')
    city = models.CharField(max_length=255)

    # state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    postal_code = models.IntegerField()

    medical_area = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=255)
    birthday = models.DateField(auto_now=False)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')
    edu_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def image_tag(self):
    #     return mark_safe('<img src="/img/%s" width="150" height="150" />' % self.image.url)
    #
    # image_tag.short_description = 'Image'
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    STATE_CHOICES = (
        ('A', 'Active'),
        ('B', 'Inactive'),
    )
    status = models.CharField(max_length=1, choices=STATE_CHOICES)

    def is_activated(self):
        if self.status == 'A':
            return True
        return False

    is_activated.boolean = True
    is_activated.short_description = "Status"

    def __str__(self):
        return self.fname + ' ' + self.lname

    class Meta:
        verbose_name = 'Doctor'

# def generate_id_length():
#     code_length = 7
#     return get_random_string(code_length).upper()


class Patient(models.Model):
    code_length = 7
    code = models.CharField(max_length=code_length, editable=False, default=generate_id_length, unique=True, verbose_name='Patient ID')
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    # name = fname + lname
    uname = models.CharField(max_length=255, verbose_name='username')
    slug = models.SlugField(max_length=255, unique=True)

    def save(self, **kwargs):
        slug = '%s' % (self.uname)
        unique_slugify(self, slug)
        super(Patient, self).save()

    disease = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # password = models.CharField(max_length=20, widget=forms.PasswordInput)
    # c_password = models.CharField(max_length=20, widget=forms.PasswordInput)

    email = models.EmailField(max_length=255)
    birthday = models.DateField(auto_now=False)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    address = models.CharField(max_length=255)

    # country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    # state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)

    city = models.CharField(max_length=255)

    postal_code = models.IntegerField()
    phone = models.IntegerField()
    image = models.ImageField(upload_to='img/patients', null=True)

    STATE_CHOICES = (
        ('A', 'Active'),
        ('B', 'Inactive'),
    )
    status = models.CharField(max_length=1, choices=STATE_CHOICES)

    def is_activated(self):
        if self.status == 'A':
            return True
        return False

    is_activated.boolean = True
    is_activated.short_description = "Status"

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    def __str__(self):
        return self.fullname


# def generate_id_length():
#     code_length = 7
#     return get_random_string(code_length).upper()


class Appointment(models.Model):
    code_length = 7
    code = models.CharField(max_length=code_length, editable=False, default=generate_id_length, unique=True, verbose_name='Appointment ID')
    # patient_name = models.CharField(max_length=255)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    # slug = models.SlugField(blank=True)
    slug = models.SlugField(max_length=140, unique=True)

    def save(self, **kwargs):
        slug = '%s' % (self.fname)
        unique_slugify(self, slug)
        super(Appointment, self).save()

    # slug = models.SlugField(max_length=255, unique=True)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=50)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    age = models.IntegerField()
    # doctor = models.ForeignKey(DocProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DocProfile, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    message = models.TextField()
    STATE_CHOICES = (
        ('A', 'Active'),
        ('B', 'Inactive'),
    )
    status = models.CharField(max_length=1, choices=STATE_CHOICES)

    def is_activated(self):
        if self.status == 'A':
            return True
        return False

    is_activated.boolean = True
    is_activated.short_description = "Status"

    @property
    # def patient_name(self):
    def fullname(self):
        return f"{self.fname} {self.lname}"

    def __str__(self):
        return self.fullname

    def _get_unique_slug(self):
        slug = slugify(self.fname)
        unique_slug = slug
        num = 1
        while Appointment.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


class Schedule(models.Model):
    code_length = 7
    code = models.CharField(max_length=code_length, editable=False, default=generate_id_length, unique=True, verbose_name='Schedule ID')
    # doc_obj = models.ForeignKey(DocProfile, on_delete=models.CASCADE, verbose_name='Doctor', null=True)
    # dep_obj = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Department', null=True)
    doc_obj = models.ForeignKey(DocProfile, on_delete=models.SET_NULL, verbose_name='Doctor', null=True)
    dep_obj = models.ForeignKey(Department, on_delete=models.SET_NULL, verbose_name='Department', null=True)
    available_days = models.ManyToManyField(Days)

    def getavailable_days(self):
        return "\n".join([p.days for p in self.available_days.all()])

    start_time = models.TimeField(auto_now=False, null=True)
    end_time = models.TimeField(auto_now=False, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATE_CHOICES = (
        ('A', 'Active'),
        ('B', 'Inactive'),
    )
    status = models.CharField(max_length=1, choices=STATE_CHOICES, default='Active')

    def is_activated(self):
        if self.status == 'A':
            return True
        return False

    is_activated.boolean = True
    is_activated.short_description = "Status"

    # def __str__(self):
    #     return self.available_days

    def __str__(self):
        return "Schedule successfully created"

    class Meta:
        ordering = ['-updated_at']


def generate_id_length():
    return get_random_string(Employee.code_length).upper()


class Employee(models.Model):
    code_length = 7
    code = models.CharField(max_length=code_length, editable=False, default=generate_id_length, unique=True, verbose_name='Employee ID')
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    uname = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, **kwargs):
        slug = '%s' % (self.uname)
        unique_slugify(self, slug)
        super(Employee, self).save()

    age = models.DateField(auto_now=False)
    image = models.ImageField(upload_to='img/Employee')
    email = models.EmailField(max_length=255)
    joining_date = models.DateField()
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
        ('Laboratorist', 'Laboratorist'),
        ('Pharmacist', 'Pharmacist'),
        ('Accountant', 'Accountant'),
        ('Receptionist', 'Receptionist'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    STATE_CHOICES = (
        ('A', 'Active'),
        ('B', 'Inactive'),
    )
    status = models.CharField(max_length=1, choices=STATE_CHOICES)

    def is_activated(self):
        if self.status == 'A':
            return True
        return False

    is_activated.boolean = True
    is_activated.short_description = "Status"

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    def __str__(self):
        return self.fullname


class EmpLeave(models.Model):
    # emp_id=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    LEAVE_CHOICES = {
        ('Casual Leave 12 Days', 'Casual Leave Type'),
        ('Medical Leave', 'Medical Leave'),
        ('Loss of Pay', 'Loss of Pay'),
    }
    leave_type = models.CharField(max_length=25, choices=LEAVE_CHOICES)
    from_date = models.DateField()
    to_date = models.DateField()
    # no_of_days=from_date - to_date
    reason = models.CharField(max_length=255)
    STATUS_CHOICES = {
        ('A', 'Approved'),
        ('D', 'Declined'),
        ('N', 'New'),
    }
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Employee Leave'

    def __str__(self):
        return self.user.fullname

    @property
    def no_of_days(self):
        total_days = (self.to_date - self.from_date).days
        leaves = total_days + 1
        total_leaves_taken = + leaves
        return leaves

    @property
    def remaining_leaves(self):
        total_leaves_days = 12
        return total_leaves_days - self.no_of_days
