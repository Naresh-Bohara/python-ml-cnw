from django.shortcuts import render
from .models import Students

# Create your views here.

def index(request):
    students = Students.objects.all()
    context = {'students': students}
    return render(request, 'index.html', context)

def home(request):
    return render(request, 'home.html')