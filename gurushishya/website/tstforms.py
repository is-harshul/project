from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='*')
    last_name = forms.CharField(max_length=30, help_text='*')
    email = forms.EmailField(max_length=254, help_text='*Inform a valid email address.')
    phone = forms.IntegerField(help_text='*Inform a valid phone number')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2', )