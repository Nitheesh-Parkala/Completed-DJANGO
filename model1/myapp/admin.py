from django.contrib import admin
from myapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    i=['eid','ename','ephone_no','esal','eplace','ejob']
       
admin.site.register(Employee,EmployeeAdmin)

