from django.shortcuts import render
from myApp.models import Student
# Create your views here.
def fakerView(request):
   s=Student.objects.all() 
   k={'stud':s}
   return render(request,'htmlpage/1.html',k)