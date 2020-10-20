from django.db import models
from django.contrib.auth.models import User

# 여성의류
class Cloth_female(models.Model):
    photo = models.ImageField(null=True, upload_to='media/')
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=15)
    size = models.CharField(max_length=15)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        managed = False    

# 남성의류
class Cloth_male(models.Model):
    photo = models.ImageField(null=True, upload_to='media/')
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=15)
    size = models.CharField(max_length=15)
    
   

    def __str__(self):
        return self.name

    class Meta:
        managed = False    


    