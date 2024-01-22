
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("following", views.following, name="following"),
    path("profile/<str:username>", views.profile, name="profile"),

    # API Routes
    path("posts/", views.posts, name="posts"),
    path("profileposts/<str:username>/", views.profileposts, name="profileposts"),
    path("manage_follower/<str:target_username>/<str:action>", views.manage_follower, name="manage_follower"),
    path("followingposts/", views.followingposts, name="followingposts"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete_post/<int:post_id>", views.delete_post, name="delete_post"),
    path("manage_likes/<int:post_id>", views.manage_likes, name="manage_likes"),
]