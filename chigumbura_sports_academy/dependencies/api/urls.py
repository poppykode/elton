from django.urls import path
from .views import add_dependent,get_dependents,delete_dependent,update_dependent

urlpatterns = [
    path('add/dependent', add_dependent),
    path('get',get_dependents),
    path('delete/<int:pk>',delete_dependent),
    path('update/<int:pk>',update_dependent),
]
