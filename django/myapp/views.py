from django.shortcuts import redirect, render
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

def student_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        marks = request.POST.get('marks')

        student = Students.objects.create(
            name=name,
            email=email,
            age=age,
            marks=marks
        )
        student.save()
        return redirect('/home/')
    return render(request, 'form.html')