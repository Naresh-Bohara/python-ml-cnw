from django.shortcuts import render

# Create your views here.
def index(request):
    data = [
        {
        'name': 'Naresh',
        'age': 25,
        'city': 'Dhangadhi',
        'marks': 58
    },
    {
        'name': 'Ravi',
        'age': 30,
        'city': 'Kathmandu',
        'marks': 90
    },
    {
        'name': 'Suresh',
        'age': 28,
        'city': 'Pokhara',
        'marks': 61
    },
    {
        'name': 'Mahesh',
        'age': 32,
        'city': 'Biratnagar',
        'marks': 85
    }
    ]
    context = {'data': data}
    return render(request, 'index.html', context)
def home(request):
    students = ["Naresh", "Ravi", "Suresh", "Mahesh"]
    context = {'students': students}
    return render(request, 'home.html', context)