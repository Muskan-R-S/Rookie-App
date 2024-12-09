from django import forms 
from .models import Mandate

class MandateForm(forms.ModelForm):
    class Meta:
        model = Mandate
        fields = ['company_name', 'requirement', 'role_name']