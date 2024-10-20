from django import forms
from .models import VentFindings,FarmerRegister

class VentFindingForm(forms.ModelForm):
    class Meta:
        model = VentFindings
        fields = ['type_of_breed', 'age', 'type_of_disease', 'symptoms', 'location']


class FarmerRegisterForm(forms.ModelForm):
    class Meta:
        model = FarmerRegister
        fields = ['name', 'email', 'phone_number', 'location']