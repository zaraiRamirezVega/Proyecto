from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Usuario', 
        max_length=100
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput
    )
    age = forms.IntegerField(
        label='Edad'
    )
    gender = forms.ChoiceField(
        label='Género',
        choices=[('hombre', 'Masculino'), ('mujer', 'Femenino')]
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuario', 
        max_length=100
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput
    )

