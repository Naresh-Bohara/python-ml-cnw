from django.shortcuts import render
from .models import Students

# Create your views here.

def index(request):
    students = Students.objects.get(id=1)
    context = {'students': students}
    return render(request, 'index.html', context)

def home(request):
    # students = Students.objects.all()
    students = Students.objects.filter(age__gt=17)

    # // student object
#     students = Students.objects.create(
#     name='John Doe',
#     age=20,
#     city='New York',
#     marks=85,
#     email='john.doe@example.com'
# )

#     for student update object
#     student = Students.objects.get(id=1)
#     student.name = 'Jane Doe'
#     student.save()

#      for student delete object
#      student = Students.objects.get(id=1)
#      student.delete()

#     for ordering
#     students = Students.objects.order_by('name')

#     for ordering in reverse
#     students = Students.objects.order_by('-name')

#     for ordering by multiple fields
#     students = Students.objects.order_by('age', 'name')



    context = {'students': students}
    return render(request, 'home.html', context)