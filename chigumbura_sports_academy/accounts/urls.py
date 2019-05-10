from django.urls import path
from .views import (
    register,view_profile,edit_profile,
    change_password,login,login_view,
    )

app_name='accounts'
urlpatterns = [
    path('login/view/', login_view,name='login_view'),
    path('login/', login,name='login'),
    path('register/', register,name='register'),
    path('view-profile/', view_profile,name='view_profile'),
    path('edit/profile/', edit_profile,name='edit_profile'),
    path('change-password/', change_password,name='change_password'),
]
