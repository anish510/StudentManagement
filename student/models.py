from django.db import models
from django.utils.text import slugify 
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    slug = models.SlugField(unique=True)
    city = models.CharField(max_length=100)
    # marks = models.IntegerField()
    dob = models.DateField(null=True)
    phone_number = models.CharField(max_length=10)
    image_url = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.slug
    
@receiver(pre_save, sender = Student)
def store_pre_save(sender,instance:Student, *args, **kwargs):
    if not instance.slug:
        if instance.name:
            rand_num = str(random.randint(00000,99999))
            instance.slug = slugify(instance.name + rand_num)
