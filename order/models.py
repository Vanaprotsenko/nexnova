from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class Bucket(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class ProductBucket(models.Model):
    count = models.IntegerField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    bucket = models.ForeignKey(
        Bucket, on_delete=models.CASCADE,
        null=True,
        blank=True
    )
