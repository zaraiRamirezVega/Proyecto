from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Usuario', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    age = forms.IntegerField(
        label='Edad',
        widget=forms.NumberInput(attrs={'class': 'form-input'})
    )
    gender = forms.ChoiceField(
        label='Género',
        choices=[('hombre', 'Masculino'), ('mujer', 'Femenino')],
        widget=forms.Select(attrs={'class': 'form-select'})
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

