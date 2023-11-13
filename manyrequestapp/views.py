from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getinput(request):
    return render(request,"getinput.html")
def postinput(request):
    return render(request,"postinput.html")
def add(request):
    if request.method=="GET":
        i=request.GET["t1"]
        j=request.GET["t2"]
        try:
            x=int(i)
            y=int(j)
            k=x+y
            return HttpResponse("SUM IS:"+str(k))
        except(ValueError):
            return HttpResponse("invalid input")
    elif request.method=="POST":
        i=request.POST["t1"]
        j=request.POST["t2"]
        try:
            x=int(i)
            y=int(j)
            k=x+y
            return HttpResponse("SUM IS:"+str(k))
        except(ValueError):
            return HttpResponse("invali input")


