from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"your name"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"your email"}))
    content=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"your content"}))

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail")
        return email

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"your user-name"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))

class RegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"your user-name"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "your email"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))

    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password!=confirm_password:
            raise  forms.ValidationError("Both PAssword need to be same")
        return data

    def clean_username(self):
        username=self.cleaned_data.get("username")
        qs=User.objects.filter(username=username)
        if qs.exist():
            raise forms.ValidationError("Username already taken")
        return username


