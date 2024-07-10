from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings 
from .forms import ContactForm
from .models import ContactMessage, Project
def index(request):
    return render(request, 'index.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'tproject.html',{'projects':projects})

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['full_name']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone_number']
            message=form.cleaned_data['message']
            
            form.save()

            return redirect('index')
    else:
        form=ContactForm()   
    return render(request, 'contact.html',{'form':form})
