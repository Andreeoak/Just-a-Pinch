from django.urls import path
from .views import *

#namespacing
app_name = 'users'

urlpatterns = [
    path('register/', register, name="register"),
]