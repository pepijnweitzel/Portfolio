from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms

from .models import User, Listing


# Create class for form to create listing
class NewListingForm(forms.Form):
    listings_title = forms.CharField(label="Listings Title", max_length=64)
    listings_description = forms.CharField(widget=forms.Textarea, label="Listings Description", max_length=1024)
    listings_starting_bid = forms.IntegerField(label="Starting Bid")
    listings_url = forms.URLField(label="Image URL", required=False)
    listings_category = forms.CharField(label="Listings Category", required=False, max_length=64)


def index(request):
    
    return render(request, "auctions/index.html", {
        "listings" : Listing.objects.all()
    })


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

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the attributes from the 'cleaned' version of form data
            title = form.cleaned_data["listings_title"]
            description = form.cleaned_data["listings_description"]
            starting_bid = form.cleaned_data["listings_starting_bid"]
            url = form.cleaned_data["listings_url"]
            category = form.cleaned_data["listings_category"]
            username = request.user

            # Save listing to database
            listing = Listing(title=title, description=description, starting_bid=starting_bid, url=url, category=category, owner=username)
            listing.save()

            # Redirect user to index page
            return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html", {
        "form" : NewListingForm(),
    })


def listing(request, listing_id):

    if request.method == "POST":
        try:

            if request.POST["watch"]:
                # Add to watchlist
                #TODO
                pass

        except KeyError:

            if request.POST["bid"]:
                # Update bid
                # Get bidded value
                bid = int(request.POST["bid"])

                # Get listing object
                listing = Listing.objects.get(id=listing_id)

                # Change the value of the bid
                listing.starting_bid = bid

                # Set highest bidder to new user
                username = request.user.username

                # Update value of bid
                listing.save()


    listing = Listing.objects.get(id=listing_id)
    return render(request, "auctions/listing.html", {
        "listing" : listing
    })
