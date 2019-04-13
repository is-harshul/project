from django import forms
# from django.contrib.auth.models import User
from . models import SignupUser
from django.core.validators import validate_email

class userform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input--style-3 cw', 'placeholder': 'Name'}), required=True, max_length=50)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input--style-3 cw', 'placeholder': 'Username'}), required=True, max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input--style-3 cw', 'placeholder': 'Email'}), required=True,)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input--style-3 cw', 'placeholder': 'Password'}),required=True,)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input--style-3 cw', 'placeholder': 'Confirm password'}),required=True,)
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input--style-3 cw', 'placeholder': 'Phone Number'}), required=True, )

    class Meta():
        model = SignupUser
        fields = ['name','username','email','password1','password2','phone']

    def clean_username(self):
        user= self.cleaned_data['username']
        try:
            match = SignupUser.objects.get(Username=user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("Username already in use.")

    def clean_phone(self):
        phone= self.cleaned_data['phone']
        try:
            match = SignupUser.objects.get(Phone=phone)
        except:
            return self.cleaned_data['phone']
        raise forms.ValidationError("Phone Number already in use.")
    
    def clean_email(self):
        email= self.cleaned_data['email']
        try:
            mt= validate_email(email)
        except:
            return forms.ValidationError("Email is not in correct format")
        try:
            match = SignupUser.objects.get(Email=email)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError("Email already in use.")
        return email
    def clean_password2(self):
        pas = self.cleaned_data['password1']
        cpas = self.cleaned_data['password2']
        if pas and cpas:
            if pas != cpas:
                raise forms.ValidationError("Password and Confirm password not matched")