from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50, blank = True, null = True)
    
