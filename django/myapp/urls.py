from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home, name="home"), 
    path('form/', views.student_form, name="form"),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),  # Changed from student_id to id
    path('delete/<int:id>/', views.delete_student, name='delete_student'),  # Changed from student_id to id
    path('child/', views.child, name='child'),
]