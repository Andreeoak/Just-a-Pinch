from django.urls import path
from .views import *

#namespacing
app_name = 'myapp'

urlpatterns = [
    path('', index, name="index"),
    path('item/', item),
    path('<int:id>/', detail, name="detail"),
]