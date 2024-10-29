from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=40)
    ephone_no=models.FloatField()
    esal=models.FloatField()
    eplace=models.CharField(max_length=50)
    ejob=models.CharField(max_length=40)
     
    def __str__(self):
        return self.ename