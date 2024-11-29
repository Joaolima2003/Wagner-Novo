from django import forms
from .models import Hospede, Reserva

class HospedeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Hospede
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class ReservaForm(forms.ModelForm): 
    class Meta: 
        model = Reserva 
        fields = ['hospede', 'data_check_in', 'data_check_out', 'tipo_quarto']