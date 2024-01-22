from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

import json

import random

from .models import User, Post


def index(request):

    return render(request, "network/index.html")


def login_view(request):

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, avatar_location="/static/network/avatars/avatar1.png")
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required
def new(request):

    # Check for method
    if request.method == "POST":

        # Acces input values
        title = request.POST["title"]
        content = request.POST["content"]

        # Create and save a new Post instance
        new_post = Post(author=request.user, title=title, content=content, timestamp=timezone.now())
        new_post.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        # If get method return the page
        return render(request, "network/new_post.html")


@login_required
def following(request):

    # Get all people user is following
    followings = request.user.following.all()

    # Get all users (exclude current user) and pick 3 random ones
    all_users = User.objects.all()
    all_users = all_users.exclude(pk=request.user.pk)
    # Get 3 random users from the list of all users
    random_users = random.sample(list(all_users), min(3, len(all_users)))

    return render(request, "network/following.html", {
        "followings" : followings,
        "randoms" : random_users,
    })


def profile(request, username):

    # Get user
    user = User.objects.get(username=username)
    # Check for method
    if request.method == "POST":

        # Acces input values
        new_username = request.POST["new_username"]
        new_email = request.POST["new_email"]

        # Get user, change properties (if exist) and save
        user = User.objects.get(username=username)
        user.username = new_username if new_username else user.username
        user.email = new_email if new_email else user.email
        user.save()

        return HttpResponseRedirect(reverse("index"))

    # Get counts
    following_count = user.following.count()
    followers_count = user.followers.count()

    # Check if request.user already follows profile_owner or not (True if already following, False if not)
    following_status = "Unfollow" if request.user in user.followers.all() else "Follow"

    return render(request, "network/profile.html", {
        "profile_owner" : user,
        "followings" : following_count,
        "followers" : followers_count,
        "following_status" : following_status,
    })


def posts(request):
    # Backend for api request

    # Get all existing posts and return in reverse chronological order
    all_posts = Post.objects.all()
    all_posts = all_posts.order_by("-timestamp").all()

    # Set number of posts on the page and paginator
    posts_per_page = 10
    paginator = Paginator(all_posts, posts_per_page)

    # Get the page number we want to be on
    page = request.GET.get("page")

    try:
        page_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results.
        page_posts = paginator.page(paginator.num_pages)

    # Return in JSON (set safe to false so any object can be serialized)
    return JsonResponse({"posts":[post.serialize() for post in page_posts], "max_pages":paginator.num_pages}, safe=False)


def profileposts(request, username):
    # Backend for api request

    # Get user for author
    author = User.objects.get(username=username)
    # Get all exisitngs posts of specific profile
    profile_posts = Post.objects.filter(author=author)

    # Return posts in reverse chronological order
    profile_posts = profile_posts.order_by("-timestamp").all()

    # Set number of posts on the page and paginator
    posts_per_page = 10
    
    paginator = Paginator(profile_posts, posts_per_page)

    # Get the page number we want to be on
    page = request.GET.get("page")

    try:
        page_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results.
        page_posts = paginator.page(paginator.num_pages)

    # Return in JSON (set safe to false so any object can be serialized)
    return JsonResponse({"posts":[post.serialize() for post in page_posts], "max_pages":paginator.num_pages}, safe=False)


@login_required
def manage_follower(request, target_username, action):
    # Backend for api request

    try:
        # Get target user
        target_user = User.objects.get(username=target_username)

        # Check what action
        if action == "Follow":
            request.user.following.add(target_user)
        elif action == "Unfollow":
            request.user.following.remove(target_user)
        # Save users following
        request.user.save()

        # Get the new count of followers
        new_count = target_user.followers.count()

        return JsonResponse({"message":f"{action}ed successfully", "newCount":new_count }, status=200)
    
    except User.DoesNotExist:
        return JsonResponse({"message":"user not found"}, status=404)


@login_required
def followingposts(request):
    # Backend for api request

    # Get user
    user = User.objects.get(username=request.user)

    # Get all users he is following
    followings = user.following.all()
    
    # Get all posts where the author is in followings
    posts_from_followings = Post.objects.filter(author__in=followings)

    # Return posts in reverse chronological order
    posts_from_followings = posts_from_followings.order_by("-timestamp").all()

    # Set number of posts on the page and paginator
    posts_per_page = 10
    
    paginator = Paginator(posts_from_followings, posts_per_page)

    # Get the page number we want to be on
    page = request.GET.get("page")

    try:
        page_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results.
        page_posts = paginator.page(paginator.num_pages)

    # Return in JSON (set safe to false so any object can be serialized)
    return JsonResponse({"posts":[post.serialize() for post in page_posts], "max_pages":paginator.num_pages}, safe=False)


@login_required
def edit(request, id):
    # Backend for api request

    try:
        # Get post to edit
        post = Post.objects.get(id=id, author=request.user)

        # Decode the JSON data from the request body
        json_data = json.loads(request.body.decode('utf-8'))

        # Get new content
        new_content = json_data.get('content')
        
        # Change old content to new and save
        post.content = new_content
        post.save()

        return JsonResponse({'message':f'post {id}, has been edited succesfully'}, status=200)
    except Post.DoesNotExist:
        return JsonResponse({'message':'post not found'}, status=404)
    

def delete_post(request, post_id):
    # Backend for api request

    try:
        # Get post to delete
        post = Post.objects.get(id=id, author=request.user)

        # Delete the post
        post.delete()

        return JsonResponse({'message':f'post {id}, has been edited succesfully'}, status=200)
    except Post.DoesNotExist:
        return JsonResponse({'message':'post not found'}, status=404)
    

@login_required
def manage_likes(request, post_id):
    # Backend for api request

    # Get post and current user
    post = Post.objects.get(id=post_id)
    user = request.user

    # Check if the user has already liked the post
    has_liked = post.likes.filter(id=user.id).exists()

    if has_liked:
        # Remove like
        post.likes.remove(user)
        return JsonResponse({'message':f'post has been unliked by {user.username}'}, status=200)
    else:
        # Make like
        post.likes.add(user)
        return JsonResponse({'message':f'post has been liked by {user.username}'}, status=200)