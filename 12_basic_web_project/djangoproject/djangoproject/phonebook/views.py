from django.shortcuts import render, redirect

def landing_function(request):
    return render(request, "phonebook/index.html")