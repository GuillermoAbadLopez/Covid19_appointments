from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Appointment
from .forms import AppointmentForm
from datetime import date

today = date.today()



# Create your views here.

def appointment(response,id):

    ls = Appointment.objects.get(id=id)

    if response.user.is_authenticated:
        if ls in response.user.appointment.all():
            
            return render(response, "main/appointment.html", {"ls":ls})
    
    return render(response, "main/wrong_view.html",{})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = AppointmentForm(response.POST)
        
        if form.is_valid():
                name = form.cleaned_data["name"]
                age = form.cleaned_data["age"]
                address = form.cleaned_data["address"]
                phone = form.cleaned_data["phone"]
                center = form.cleaned_data["center"]
                date = form.cleaned_data["date"]

                if (date>today):
                    if (18 <= int(age) <= 100): 
                        
                        appoint = Appointment(name=name,age=age,address=address,phone=phone,center=center,date=date,confirmation_code="")
                        appoint.save()
                        response.user.appointment.add(appoint)
                        
                        return HttpResponseRedirect("/%i" %appoint.id)
                    
                    else:
                        error_message = 'You must be between 18 and 100 years old to receive a vaccination'
                        return render(response, 'main/error.html', {'error_message': error_message})
                else:
                    error_message = 'The selected date must be from tomorrow onwards'
                    return render(response, 'main/error.html', {'error_message': error_message})

    else:
        form = AppointmentForm()

    return render(response, "main/create.html", {"form":form})

def list(response):
    return render (response, "main/list.html", {})