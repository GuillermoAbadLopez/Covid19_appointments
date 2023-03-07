from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        else:  
            error_message = 'Invalid inputs, try again'
            return render(response, 'main/error.html', {'error_message': error_message})
        
        return redirect("/")

    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})