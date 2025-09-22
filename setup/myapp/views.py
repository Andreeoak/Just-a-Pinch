from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required

@login_required
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
    item = get_object_or_404(Item, id =id)
    form = ItemForm(request.POST or None, instance=item)
    
    if(form.is_valid()):
        form.save()
        return redirect('myapp:index')
    
    context = {
        "form" : form
    }
    return render(request, 'myapp/update_item.html', context)
    
def delete_item(request, id):
    item = get_object_or_404(Item, id =id)
    
    if(request.method == "POST"):
        item.delete()
        return redirect('myapp:index')
    
    return render(request, 'myapp/delete_item.html') 
