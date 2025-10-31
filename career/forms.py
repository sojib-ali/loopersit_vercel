from django import forms
from .models import Application, Job


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['role','name', 'email', 'mobile_number', 'salary_expectation', 'cv']