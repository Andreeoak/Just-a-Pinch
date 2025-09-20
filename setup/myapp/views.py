from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.
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

def item(request):
    return HttpResponse("item view")