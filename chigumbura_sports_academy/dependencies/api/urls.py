from django.urls import path
from .views import add_dependent,get_dependents,delete_dependent,update_dependent,get_videos

urlpatterns = [
    path('add/dependent', add_dependent),
    path('get/dependencies',get_dependents),
    path('delete/<int:pk>',delete_dependent),
    path('update/<int:pk>',update_dependent),
    path('get/videos/',get_videos),
]
