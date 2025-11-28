from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
        fname=models.CharField(max_length=100)
        lname=models.CharField(max_length=50)
        phone=models.CharField(max_length=20)

        
        def __str__ (self):
         return self.username