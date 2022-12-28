from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms

class HomeView(generic.ListView):
    model = models.Service
    template_name = 'home.html'

class ServiceDetailView(generic.DetailView):
    model = models.Service
    template_name = 'service-detail.html'

class ContactView(SuccessMessageMixin, generic.CreateView):
    success_url = reverse_lazy('service:contact')
    success_message = 'Size en yakın zamanda dönüş sağlayacağız. Teşekkür ederiz!'
    form_class = forms.FeedbackRequestForm
    model = models.FeedbackRequest
    template_name = 'contact.html'

