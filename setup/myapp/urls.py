from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('item/', item),
    path('<int:id>/', detail),
]