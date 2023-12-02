from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .forms import TeleMedUserCreationForm, TeleMedUserChangeForm
from .models import TeleMedUser, DocSpecialty, Doctor, Patient, DocAvailableDate


class TeleMedUserAdmin(UserAdmin):
    add_form = TeleMedUserCreationForm
    form = TeleMedUserChangeForm


    list_display = ['first_name', 'last_name', 'email', 'phone', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Personal info', {'fields': ['first_name', 'last_name', 'phone']}),
        ('Permissions', {'fields': ['is_admin']}),
    ]


    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['first_name', 'last_name', 'email', 'phone', 'password1', 'password2'],
        }),
    ]

    search_fields = ['email',]
    ordering = ['email',]
    filter_horizontal = []



admin.site.register(TeleMedUser, TeleMedUserAdmin)
admin.site.register(DocSpecialty)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(DocAvailableDate)


