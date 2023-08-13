from django.shortcuts import render
from base_app.models import Hero_section
from base_app.models import About_us

# Create your views here.
def index(request):
    """request for home page"""
    hero_section = Hero_section.objects.all()
    about_data = About_us.objects.all()
    
    context = {
        "hero_section": hero_section,
        "about_data": about_data,
    }
    
    return render(request, 'index.html', context)