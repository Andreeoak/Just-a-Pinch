from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def register(request):
    context ={
        "form" : UserCreationForm()
    }
    return render(request, 'users/register.html', context)