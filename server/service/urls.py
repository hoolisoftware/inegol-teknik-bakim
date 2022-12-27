from django.urls import path

from . import views

app_name = 'service'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('services/<int:pk>', views.ServiceDetailView.as_view(), name='service-detail'),
    path('contact', views.ContactView.as_view(), name='contact'),
]