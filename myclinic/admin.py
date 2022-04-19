from django.contrib import admin
from django.utils.html import format_html

from .models import *


# Register your models here.
@admin.register(DocProfile)
class AdminDocProfile(admin.ModelAdmin):
    # list_display = ['name', 'gender', 'medical_area', 'emp_id', 'phone', 'address', 'image_tag']
    # fields = ['image_tag']
    # readonly_fields = ['image_tag']

    # To display the image in admin
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['code', 'fullname', 'created_at', 'country', 'gender', 'medical_area', 'phone', 'address', 'is_activated',
                    'image_tag']
    prepopulated_fields = {'slug': ('fname',)}


@admin.register(Patient)
class AdminPatient(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['fullname', 'uname', 'created_at', 'birthday', 'country', 'phone', 'address', 'is_activated', 'slug', 'image_tag']
    prepopulated_fields = {'slug': ('uname',)}
    #
    # def fullname(self, obj):
    #     first=Patient.fname
    #     last=Patient.lname
    #
    #     # return '{} {}'.format(Patient.fname, Patient.lname)
    #     # return  '{} {}'.join(Patient.fname,Patient.lname)
    #     return (fullname)


@admin.register(Appointment)
class AdminAppointment(admin.ModelAdmin):
    list_display = ['code', 'fullname', 'id', 'age', 'department', 'doctor', 'date', 'time', 'email', 'phone',
                    'status', 'is_activated']
    prepopulated_fields = {'slug': ('fname',)}


@admin.register(Country)
class AdminCountry(admin.ModelAdmin):
    list_display = ['country']


@admin.register(State)
class AdminCountry(admin.ModelAdmin):
    list_display = ['state']


@admin.register(Department)
class AdminDepartment(admin.ModelAdmin):
    list_display = ['department', 'is_activated']


@admin.register(Days)
class AdminDays(admin.ModelAdmin):
    list_display = ['id', 'days']


@admin.register(Schedule)
class AdminSchedule(admin.ModelAdmin):
    # list_display = ['doc_obj','dep_obj','available_days','is_activated']
    list_display = ['doc_obj', 'dep_obj', 'created_at', 'getavailable_days', 'is_activated']
    # prepopulated_fields = {'slug': ('doc_obj',)}


# @admin.register(Employee)
# class AdminEmployee(admin.ModelAdmin):
#     list_display = ['code', 'fullname', 'phone', 'email', 'joining_date', 'role', 'status', 'is_activated', 'image_tag']
#     prepopulated_fields = {'slug': ('uname',)}
#
#     def image_tag(self, obj):
#         return format_html('<img src="{}" width="100" height="100"/>'.format(obj.image.url))


@admin.register(Departmentzz)
class AdminDepartment(admin.ModelAdmin):
    list_display = ['department', 'description', 'is_activated']


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100"/>'.format(obj.image.url))

    list_display = ['fullname', 'uname', 'role', 'gender', 'email', 'joining_date', 'phone', 'role', 'status', 'image_tag']
    # prepopulated_fields = {'slug': ('fname',)}
    prepopulated_fields = {'slug': ('uname',)}


@admin.register(EmpLeave)
class AdminEmpLeave(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100"/>'.format(obj.image.url))

    list_display = ['user', 'leave_type', 'from_date', 'to_date', 'reason', 'status']
