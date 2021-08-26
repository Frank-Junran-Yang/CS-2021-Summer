from django.db import models
from student.models import Student
from teacher.models import Teacher


class Lesson(models.Model):
    name = models.CharField(max_length = 30)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank = True, null = True)
    students = models.ManyToManyField(Student)