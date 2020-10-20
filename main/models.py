from django.db import models

# Create your models here.

# 여성의류
class Cloth_female(models.Model):
    photo = models.ImageField(null=True)
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    price = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    size = models.CharField(max_length=15)

    # def __str__(self):
    #     return name

# 남성의류
class Cloth_male(models.Model):
    photo = models.ImageField(null=True)
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    price = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    size = models.CharField(max_length=15)

    # def __str__(self):
    #     return name
    