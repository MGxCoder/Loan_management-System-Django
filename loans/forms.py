from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'name', 'age', 'contact_no', 'city', 'cibil_score', 'income',
            'employment_status', 'loan_term', 'loan_amount',
            'residential_assets', 'commercial_assets'
        ]
