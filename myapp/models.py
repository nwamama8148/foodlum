from tokenize import group
from django.db import models
from autoslug import AutoSlugField
# from django.contrib.auth.models import AbstractUser

# Create your models here.

class FoodProduct(models.Model):
    name  = models.CharField( max_length=50)
    img = models.ImageField(upload_to='img/food_product')
    date_of_creation = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    slug = AutoSlugField(populate_from='name', unique=True, max_length=150)
    is_lunch = models.BooleanField(default=False)
    is_breakfast = models.BooleanField(default=False)
    is_dinner = models.BooleanField(default=False)
    is_best = models.BooleanField(default=True)
    
    class Meta:
        """Meta definition for FoodProduct."""

        verbose_name = 'FoodProduct'
        verbose_name_plural = 'FoodProducts'

    def __str__(self):
        return self.name

class Team(models.Model):
    full_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    img = models.ImageField(upload_to='img/team')

# class CustomUser(AbstractUser):
#    firstname = models.CharField(max_length=50)
#    lastname = models.CharField(max_length=50)
#    username = models.CharField(max_length=50)
#    password1 = models.CharField(max_length=50)
#    password2= models.CharField(max_length=50)
   


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    orders = models.TextField()
    nop = models.IntegerField()
    special_request = models.TextField()

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.name