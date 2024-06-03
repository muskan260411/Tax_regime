from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, TaxRegime

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ( 'username', 'email', 'contact_number','employee_id', 'password1', 'password2')

class CustomUserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class TaxRegimeForm(forms.ModelForm):
    class Meta:
        model = TaxRegime
        fields = ['regime_choice']
        widgets = {
            'regime_choice': forms.RadioSelect
        }

        

