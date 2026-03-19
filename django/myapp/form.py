from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}))
    marks = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your marks'}))
    city = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}))
    email = forms.CharField(max_length=100,
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))