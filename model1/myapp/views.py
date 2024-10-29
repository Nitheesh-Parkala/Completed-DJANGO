from django.shortcuts import render
from myapp.models import Employee
# Create your views here.

def myView(request):
   e=Employee.objects.all()
   d={'emp': e}
   return render(request, 'htmlpage/1.html',d)
