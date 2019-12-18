from django.shortcuts import render, redirect


# Create your views here.

def hello(request):
    return render(request, 'locatio.html', {"object": 144})
