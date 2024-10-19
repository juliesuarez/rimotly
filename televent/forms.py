from django import forms
from .models import VentFindings

class VentFindingForm(forms.ModelForm):
    class Meta:
        model = VentFindings
        fields = ['type_of_breed', 'age', 'type_of_disease', 'symptoms', 'location']
