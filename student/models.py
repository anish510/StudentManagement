from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    marks = models.IntegerField()
    dob = models.DateField()
    phone_number = PhoneNumberField(null = False, blank = False ,unique = True)

    def __str__(self):
        return self.name
