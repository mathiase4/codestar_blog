from django.shortcuts import render
from .models import about 

# Create your views here.

def about_me(request):
    
    about = about.objects.all().order_by('-updated_on').first()
    
    return render(
        request,
        "about/about.html",
        {"about": about},
        
    )