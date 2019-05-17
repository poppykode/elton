from django.urls import path
from .views import get_sports_categories

urlpatterns = [
    path('get/get_sports_categories', get_sports_categories),
]
