from django.urls import path
from .views import (
    login,sample_api,register,logout,
    )


urlpatterns = [
    path('login', login),
    path('logout', logout),
    path('sample_api', sample_api),
    path('register', register),
]