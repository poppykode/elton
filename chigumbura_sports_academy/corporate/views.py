from django.shortcuts import render
from .models import Event

# Create your views here.
def index(request):
    template_name = 'corporate/index.html'
    qs = Event.objects.all()
    context ={'events':qs}
    return render(request,template_name,context)

def about_elton(request):
    template_name = 'corporate/about_elton.html'
    return render(request,template_name)

def about_us(request):
    template_name = 'corporate/about_us.html'
    return render(request,template_name)

def join_academy(request):
    template_name = 'corporate/join_academy.html'
    return render(request,template_name)

def events(request):
    template_name = 'corporate/events.html'
    return render(request,template_name)

def contact_us(request):
    template_name = 'corporate/contact_us.html'
    return render(request,template_name)

def donate(request):
    template_name = 'corporate/donate.html'
    return render(request,template_name)
