from django.shortcuts import render
from .models import Teacher

def all_teachers(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers' : teachers
    }

    return render(request, 'teacher/all.jinja', context)