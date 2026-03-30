from django.shortcuts import get_object_or_404, redirect, render

from myapp.form import StudentForm
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

# def student_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         age = request.POST.get('age')
#         marks = request.POST.get('marks')
#         city = request.POST.get('city')

#         student = Students.objects.create(
#             name=name,
#             email=email,
#             age=age,
#             marks=marks,
#             city=city
#         )
#         student.save()
#         return redirect('/home/')
#     return render(request, 'form.html')

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  
        
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            student = Students.objects.create(
                name=data['name'],
                email=data['email'],
                age=data['age'],
                city=data['city'],
                marks=data['marks'],
                image=data['image'] 
            )
            return redirect('home')  # Use name instead of hardcoded path

    else:
        form = StudentForm()
    
    context = {
        'form': form,
        'is_edit': False,  # Indicates this is for adding new student
        'title': 'Add New Student'
    }
    return render(request, 'form.html', context)

def edit_student(request, id):  # Changed from student_id to id
    student = get_object_or_404(Students, id=id)  # Use id here too
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    
    context = {
        'form': form,
        'student': student,
        'is_edit': True,
        'title': f'Edit Student: {student.name}'
    }
    return render(request, 'form.html', context)

def delete_student(request, id):  # Also fix delete_student
    student = get_object_or_404(Students, id=id)
    
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    
    context = {'student': student}
    return render(request, 'delete_student.html', context)

def child(request):
    return render(request, 'myapp/child.html')
