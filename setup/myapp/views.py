from django.shortcuts import render, redirect
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
    form = ItemForm(request.POST or None)
    
    if(request.method == "POST" and form.is_valid()):
        form.save()
        return redirect('myapp:index')
    
    context = {
        "form" : form
    }
    return render(request, 'myapp/item_form.html', context) 

def update_item(request, id):
    item = Item.objects.get(id =id)
    form = ItemForm(request.POST or None, instance=item)
    
    if(form.is_valid()):
        form.save()
        return redirect('myapp:index')
    
    context = {
        "form" : form
    }
    return render(request, 'myapp/update_item.html', context)
    