from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse("About Me Page - Ritesh")

def about_page(request):
    context={
        "name": "Ritesh",
        "age": 21,
    }
    return render(request, "pages/about.html",context)