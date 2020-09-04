from django.shortcuts import render

def home(request):
    return render(request, '<h1>Hello</h1>')
