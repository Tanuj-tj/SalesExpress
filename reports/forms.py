from django import forms
from reports.models import Report

class ReprotForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('name','remarks')