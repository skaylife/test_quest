from django.shortcuts import render
from django.db import connection, reset_queries

def index(request):
    return render(request, 'index.html')
    
def contact(request):
    return render(request, 'contact.html')
    
def about(request):
    return render(request, 'about.html')

def history(request):
    return render(request, 'about/history.html')