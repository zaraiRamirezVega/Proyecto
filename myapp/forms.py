from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('hombre', 'Male'), ('mujer', 'Female')])

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
