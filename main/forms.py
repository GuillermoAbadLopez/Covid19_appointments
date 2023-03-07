from django import forms
import datetime

centers = [
    ('Sant Pau', 'Sant Pau'),
    ('Vall Hebron', 'Vall Hebron'),
    ('Dexeus Quiron', 'Dexeus Quiron'),
]

class AppointmentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=300)
    age = forms.IntegerField (label = "Enter your age")
    address = forms.CharField (label = 'Enter your address' , max_length=300)
    phone = forms.CharField(label='Enter your phone number', max_length=9)
    center = forms.CharField(label='Enter your preferred vaccination center', widget=forms.Select(choices=centers))
    date = forms.DateField(initial=datetime.date.today,label='Enter your preferred vaccination date',widget=forms.SelectDateWidget() )
