from django.contrib import admin
from myApp.models import Student 
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    l=['sno','sname','smarks','saddr']
admin.site.register(Student,StudentAdmin)
