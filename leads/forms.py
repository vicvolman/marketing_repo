from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'full_name',
            'company',
            'job_title',
            'email',
            'phone_number',
            'source',
            'status',
            'estimated_value',
            'next_follow_up',
            'notes',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'source': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'estimated_value': forms.NumberInput(attrs={'class': 'form-control'}),
            'next_follow_up': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class PublicLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'full_name',
            'email',
            'phone_number',
            'company',
            'job_title',
            'tourism_focus',
            'project_stage',
            'funding_needs',
            'source',
            'notes',
        ]
        widgets = {
            # Your existing widgets
            'tourism_focus': forms.Select(attrs={'class': 'form-control'}),
            'project_stage': forms.Select(attrs={'class': 'form-control'}),
            'funding_needs': forms.Select(attrs={'class': 'form-control'}),
        }