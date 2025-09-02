from django.shortcuts import render
from .models import about as About

# Create your views here.

def about_me(request):
    about_obj = About.objects.order_by('-updated_on').first()
    
    return render(request,
        "about/about.html",
        {"about": about_obj})
    