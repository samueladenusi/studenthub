from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student

        fields = [
            'first_name',
            'last_name',
            'matric_number',
            'email',
            'department',
            'level',
            'gender',
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter first name',
                'class': "form-input"
            }),
            
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter first name',
                'class': "form-input"
            }),
            
            'matric_number': forms.TextInput(attrs={
                'placeholder': 'Enter last name',
                'class': "form-input"
            }),
            
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email address',
                'class': 'form-input'
            }),
            
            'department': forms.TextInput(attrs={
                'placeholder': 'Enter department',
                'class': 'form-input'
            }),
            
            'level': forms.NumberInput(attrs={
                'placeholder': 'Enter student level',
                'class': 'form-input'
            }),
            
            'gender': forms.Select(attrs={
                'class': 'form-input'
            })
            
        }