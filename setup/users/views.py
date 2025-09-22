from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been successfully created!')
            return redirect("users:login")
    else:
        form = RegisterForm() 

    context = {
        "form": form
    }
    return render(request, "users/register.html", context)

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')