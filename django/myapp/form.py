from django import forms
from myapp.models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'age', 'marks', 'city', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control name-input',
                'placeholder': 'Enter your name',  # Added comma here
                'id': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control email-input',
                'placeholder': 'Enter your email',
                'id': 'email'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control age-input',
                'placeholder': 'Enter your age',
                'id': 'age'
            }),
            'marks': forms.NumberInput(attrs={      
                'class': 'form-control marks-input',
                'placeholder': 'Enter your marks',
                'id': 'marks'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control city-input',
                'placeholder': 'Enter your city',
                'id': 'city'
            }),
        }