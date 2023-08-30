from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('services/<sr1>', views.s1, name='s1'),
    path('contact', views.contact, name='contact'),
    path('flights', views.flights, name='flights'),
    path('details', views.details, name='details'),
    path('test', views.test, name='test'),
    path('ticket', views.ticket, name='ticket'),
    path('fbooking', views.fbooking, name='fbooking'),
]

