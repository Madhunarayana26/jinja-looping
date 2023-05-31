from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'ashu'}
    return render(request,'loop.html',d)
def loop1(request):
    d={'name':''}
    return render(request,'loop1.html',d)