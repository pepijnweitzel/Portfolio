from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    starting_bid = models.IntegerField()
    url = models.CharField(max_length=1024, default="https://www.google.com/url?sa=i&url=http%3A%2F%2Fbeepeers.com%2Fassets%2Fimages%2Fcommerces%2F&psig=AOvVaw0CXks0Pp84eKZkY5nVy9Q8&ust=1701875483635000&source=images&cd=vfe&ved=0CBIQjRxqFwoTCJj7vK_K-IIDFQAAAAAdAAAAABAE")
    category = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")

    def __str__(self):
        return f"{self.title} selling for ${self.starting_bid}."

