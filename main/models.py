from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
import random
import string

# Create your models here.

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointment", null=True)
    name = models.CharField(max_length=300)
    age = models.IntegerField(default=0, blank=False)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=9)
    center = models.CharField(max_length=50)
    date = models.DateField()
    confirmation_code = models.CharField(max_length=8, unique=True)

    def save(self, *args, **kwargs):
        if not self.confirmation_code:
            self.confirmation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}'s vaccination appointment"