from django.shortcuts import render

# Create your views here.
def h1(request):
    return render(request,'h1.html')
def htm(request):
    return render(request,'htm.html')