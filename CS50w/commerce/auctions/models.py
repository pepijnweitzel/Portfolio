from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    starting_bid = models.IntegerField()
    url = models.URLField()
    category = models.CharField(max_length=64)
    user = models.


    def __str__(self):
        return f"{self.title} selling for ${self.starting_bid}."
