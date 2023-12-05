from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    starting_bid = models.IntegerField()
    url = models.CharField(max_length=1024, default="https://cdn.vectorstock.com/i/1000x1000/79/45/product-image-default-thumbnail-icon-graphic-web-vector-49027945.webp")
    category = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")

    def __str__(self):
        return f"{self.title} selling for ${self.starting_bid}."

