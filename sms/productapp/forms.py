from django import forms
from productapp.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'quantity', 'image']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border rounded-lg px-3 py-2',
                'placeholder': 'Enter product name'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full border rounded-lg px-3 py-2'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full border rounded-lg px-3 py-2',
                'placeholder': 'Enter price'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'w-full border rounded-lg px-3 py-2',
                'placeholder': 'Enter quantity'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full border rounded-lg px-3 py-2'
            }),
        }