from django.shortcuts import render
from .models import Teacher, Course, Student


def index(request):
    return render(request, 'main_academy/home.html')


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html')


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html')