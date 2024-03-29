from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):

    FUN = 'Fun'
    INSIDE = 'Inside'
    OUTSIDE = 'Outside'
    COMPUTER = 'Computer'

    CATEGORY_CHOICES = [
        (FUN, 'Fun'),
        (INSIDE, 'Inside'),
        (OUTSIDE, 'Outside'),
        (COMPUTER, 'Computer'),
    ]

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    starting_bid = models.IntegerField()
    url = models.CharField(max_length=1024)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    highest_bidder = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="watchlist")
    closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} selling for ${self.starting_bid}, url: {self.url}"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=1024)
    location = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="location")

    def __str__(self):
        return f"{self.author} said on {self.location.title}: {self.text}"

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
    location = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
