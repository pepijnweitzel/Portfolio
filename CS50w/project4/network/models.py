from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Self because reffering to same model, symmetrical because if A follows B, B doesnt have to follow A
    followers = models.ManyToManyField("self", symmetrical=False, blank=True, related_name='following')
    avatar_location = models.CharField(max_length=255, default="/static/network/avatars/avatar1.png")

class Post(models.Model):
    author = models.ForeignKey("User", on_delete=models.PROTECT, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="liked_posts", default = 0)

    def serialize(self):
        return {
            "id": self.id,
            "avatarLocation": self.author.avatar_location,
            "author": self.author.username,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "likesCount" : self.likes.count(),
            "likers" : [user.username for user in self.likes.all()],
        }