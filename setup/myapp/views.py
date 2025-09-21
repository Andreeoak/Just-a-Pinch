from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm


def index(request):
    context = {
        "item_list" : Item.objects.all()
    }
    return render(request, "myapp/index.html", context)

def detail(request, id):
    context = {
        "item": Item.objects.get(id=id),
    }
    return render(request, "myapp/detail.html", context)

def create_item(request):
    context = {
        "form" : ItemForm()
    }
    return render(request, 'myapp/item_form.html', context) 
    