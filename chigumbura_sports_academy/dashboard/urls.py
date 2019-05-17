from django.urls import path
from .views import dashboard_menu

app_name='dashboard'
urlpatterns = [
    path('menu', dashboard_menu,name='dashboard_menu'),
]