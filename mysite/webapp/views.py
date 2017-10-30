from django.shortcuts import render

# Create your views here.

def index(request):
    """handles request"""
    return render(request, 'webapp/home.html')
