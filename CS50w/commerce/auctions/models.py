from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    starting_bid = models.IntegerField()
    url = models.URLField(default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fdefault-image&psig=AOvVaw1Kvv7J5_E-uzKGQxKkdMnw&ust=1701874811903000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOjM_-7H-IIDFQAAAAAdAAAAABAE")
    category = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")

    def __str__(self):
        return f"{self.title} selling for ${self.starting_bid}."

