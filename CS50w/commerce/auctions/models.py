from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    starting_bid = models.IntegerField()
    url = models.URLField(default="https://images.app.goo.gl/B3o7pWxL7rVi7wHs9")
    category = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")

    def __str__(self):
        return f"{self.title} selling for ${self.starting_bid}."

