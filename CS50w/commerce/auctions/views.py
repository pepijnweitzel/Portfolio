from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms

from .models import User


# Create class for form to create listing
class NewListingForm(forms.Form):
    listings_title = forms.CharField(label="Listings Title")
    listings_description = forms.CharField(widget=forms.Textarea, label="Listings Description")
    listings_starting_bid = forms.IntegerField(label="Starting Bid")
    listings_url = forms.URLField(label="Image URL", required=False)
    listings_category = forms.CharField(label="Listings Category", required=False)


def index(request):
    return render(request, "auctions/index.html")


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewListingForm(request.POST)

        print("coming")

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the attributes from the 'cleaned' version of form data
            title = form.cleaned_data["listings_title"]
            description = form.cleaned_data["listings_description"]
            starting_bid = form.cleaned_data["listings_starting_bid"]
            url = form.cleaned_data["listings_url"]
            category = form.cleaned_data["listings_category"]

            print(title, description, starting_bid, url, category)
            # Update database and sent user to index
            return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html", {
        "form" : NewListingForm(),
    })
