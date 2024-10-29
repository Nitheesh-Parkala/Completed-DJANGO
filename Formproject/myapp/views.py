from django.shortcuts import render
from myapp.forms import StudnetForm
# Create your views here.
def FormView(request):
    f=StudnetForm()
    if request.method=="POST":
        f=StudnetForm(request.POST)
        if f.is_valid():
            name=f.cleaned_data['name']
            usn=f.cleaned_data['usn']
            mob=f.cleaned_data['mob']
            branch=f.cleaned_data['branch']
            gmail=f.cleaned_data['gmail']
            d={'name':name,'usn':usn,'mob':mob,'branch':branch,'gmail':gmail}
            return render(request,'htmlpage/output.html',d)
    d={'form':f}
    return render(request,'htmlpage/input.html',d)