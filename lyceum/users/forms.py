from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Birthday, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = ("birthday",)
        widgets = {"birthday": forms.DateInput(attrs={"type": "date"})}
