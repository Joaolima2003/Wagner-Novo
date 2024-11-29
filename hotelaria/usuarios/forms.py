from django import forms
from .models import Hospede, Reserva
from django.utils import timezone


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
        fields = ['data_check_in', 'data_check_out', 'tipo_quarto']
        widgets = { 'data_check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), 
                   'data_check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), }

    def clean_data_check_in(self):
        data_check_in = self.cleaned_data['data_check_in']
        if data_check_in < timezone.now().date():
            raise forms.ValidationError("A data de check-in não pode ser no passado.")
        return data_check_in

    def clean_data_check_out(self):
        data_check_out = self.cleaned_data['data_check_out']
        if data_check_out < timezone.now().date():
            raise forms.ValidationError("A data de check-out não pode ser no passado.")
        return data_check_out

    def clean(self):
        cleaned_data = super().clean()
        data_check_in = cleaned_data.get('data_check_in')
        data_check_out = cleaned_data.get('data_check_out')

        if data_check_in and data_check_out and data_check_in > data_check_out:
            raise forms.ValidationError("A data de check-out deve ser posterior à data de check-in.")
