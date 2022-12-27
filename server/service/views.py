from django.shortcuts import render
from django.views import generic

from .models import Service

class HomeView(generic.ListView):
    model = Service
    template_name = 'home.html'

class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'service-detail.html'

class ContactView(generic.TemplateView):
    template_name = 'contact.html'

