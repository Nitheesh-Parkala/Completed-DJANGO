from django.shortcuts import render

# Create your views here.
def  myView(request):
    myName="Nitheesh"
    favplayer="MSD"
    favAnimal="Monkey"
    favSub="Python"
    d={'Name':myName,'Player':favplayer,'Animal':favAnimal,'subject':favSub}
    return render(request,'htmlpage/home.html',d)