from django.urls import path
from .views import (
    index,about_elton,about_us,join_academy,
    events,contact_us,donate,
)

app_name='corporate'
urlpatterns = [
    path('', index, name='home'),
    path('about-elton-chigumbura', about_elton,name='about_elton'),
    path('about-us', about_us,name='about_us'),
    path('join-sports-academy', join_academy,name='join_academy'),
    path('events', events,name='events'),
    path('contact-us', contact_us,name='contact_us'),
    path('donate', donate,name='donate'),
]