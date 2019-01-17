from django import forms
from bikes.models import registrations

class registration_form(forms.ModelForm):
    class Meta():
        model=registrations
        fields = '__all__'
