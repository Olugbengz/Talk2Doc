from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import TeleMedUser


class TeleMedUserCreationForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()


    class Meta:
        model = TeleMedUser
        fields = ['first_name', 'last_name', 'email', 'phone']


    def clean_password2(self):
        password1 = self.cleaned_data.get(password1)
        password2 = self.cleaned_data.get(password2)
        if (password1 and password2) and password1 != password2:
            raise ValidationError("Your passwords don't match, retype the passwords.")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    


class TeleMedUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField

    class Meta:
        model = TeleMedUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'is_active', 'is_admin']


