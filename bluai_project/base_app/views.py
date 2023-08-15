from django.shortcuts import render, redirect
from base_app.models import Hero_section
from base_app.models import About_us
from base_app.models import MainServices
from base_app.models import Services
from base_app.models import Team
from base_app.models import Questions
from base_app.models import Details
from base_app.models import Contact_Us
from base_app.models import Accounts
from django.contrib import messages

# Create your views here.
def index(request):
    """request for home page"""
    hero_section=Hero_section.objects.all()
    about_data=About_us.objects.all()
    MainServices_data=MainServices.objects.all()
    services_data=Services.objects.all()
    team=Team.objects.all()
    questions=Questions.objects.all()
    details=Details.objects.all()
    accounts=Accounts.objects.all()
    

    context = {
        "hero_section": hero_section,
        "about_data": about_data,
        "main_service_data": MainServices_data,
        "services_data": services_data,
        "teams":team,
        "question":questions,
        "details":details,
        "accounts":accounts,
    }
    
    return render(request, 'index.html', context)

def muu(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        query = Contact_Us(name=name, email=email, subject=subject, message=message)
        query.save()
        messages.success(request, "your message was submitted successfully we will get back to you via email")
        return redirect('index')
    return render(request, 'contact.html')