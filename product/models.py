from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    diagonal = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    category = models.ManyToManyField(Category)
