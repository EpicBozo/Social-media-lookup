from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app1/index.html')

def results(request):
    return render(request, 'app1/results.html')