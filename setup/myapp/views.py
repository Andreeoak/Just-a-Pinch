from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.
def index(request):
    menu_list = Item.objects.all()
    return HttpResponse(menu_list)