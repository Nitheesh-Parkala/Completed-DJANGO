from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    marks=models.IntegerField()
    dob=models.DateField()
    email=models.EmailField()
    def __str_(self):
        return self.name
    