from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been successfully created!')
            return redirect("myapp:index")
    else:
        form = UserCreationForm() 

    context = {
        "form": form
    }
    return render(request, "users/register.html", context)