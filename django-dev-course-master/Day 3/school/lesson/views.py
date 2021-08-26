from django.shortcuts import render
from .models import Lesson

def all_lessons(request):
    context = {
        'lessons': Lesson.objects.all()
    }


    # a = Student.objects.get(id = 1)
    # b = Lesson.objects.get(id = 1)
    # b.students.add(a)
    # b.students.all()


    return render(request, 'lesson/all.jinja', context)
