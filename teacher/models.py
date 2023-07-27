from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
import random
from datetime import date
from department.models import Department

# Create your models here.
class Teacher(models.Model):
    
    name = models.CharField(max_length=100)
    dep_name = models.OneToOneField(
        Department,
        on_delete=models.PROTECT,    
        
    )
    slug = models.SlugField(unique=True)
    position = models.CharField(max_length=100)
    dob = models.DateField(default= date.today)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    image_url = models.ImageField(null=True)

    def __str__(self):
        return self.slug
    
@receiver(pre_save, sender = Teacher)
def store_pre_save(sender,instance:Teacher, *args, **kwargs):
    if not instance.slug:
        if instance.name:
            rand_num = str(random.randint(00000,99999))
            instance.slug = slugify(instance.name + rand_num)
