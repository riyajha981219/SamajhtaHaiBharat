from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Map(models.Model):
    name=models.CharField(max_length=64, unique=True)
    area= models.IntegerField(default=0)
    population = models.PositiveIntegerField()
    unemployment_female = models.FloatField()
    unemployment_male = models.FloatField()
    crime = models.FloatField()
    gdp= models.IntegerField()
    members=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name}"

class Member(models.Model):
    user= models.ForeignKey(CustomUser,on_delete= models.CASCADE,related_name="members", default=0)
    community= models.ManyToManyField(Map, related_name="communities")
    nickname= models.CharField(max_length=64,unique=True)
    profilepic= models.ImageField(blank=True, upload_to="images/")
    bio=models.TextField()
    
    def __str__(self):
        return f"{self.nickname}"
    

    



