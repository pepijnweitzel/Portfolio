from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Listing, Comment, Bid



# Create class for form to create listing
class NewListingForm(forms.Form):
    listings_title = forms.CharField(label="Listings Title", max_length=64)
    listings_description = forms.CharField(widget=forms.Textarea, label="Listings Description", max_length=1024)
    listings_starting_bid = forms.IntegerField(label="Starting Bid")
    listings_url = forms.URLField(label="Image URL", required=False)
    listings_category = forms.ChoiceField(choices=Listing.CATEGORY_CHOICES, required=False, label="Listings Category")



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

    # Get listing based on id
    listing = Listing.objects.get(id=listing_id)

    # Try to get the user
    try:
        user = User.objects.get(username=request.user.username)
    except ObjectDoesNotExist:
        in_watchlist = None
    else:
        # Get user's listings from his watchlist if any
        all_listings = user.watchlist.all()

        # Check if listing is in user's watchlist
        in_watchlist = True if listing in all_listings else None

    if request.method == "POST":

        # Check if in watchlist
        button_kind = "remove_watch" if in_watchlist else "watch"

        # Try to do button call, if error gets raised, a bid or comment has been placed or owner wants to close listing
        try:

            if request.POST[button_kind]:

                if in_watchlist:
                    # Del from watchlist
                    listing.watchlist.remove(user)

                else:
                    # Add listing to the watchlist
                    listing.watchlist.add(user)

                # Return listings page with GET request
                return HttpResponseRedirect(reverse("listing", args=[listing.id]))

        except KeyError:

            # Check if it is the owner thats on the page
            try:
                # Check if user is the owner, if so check if the owner closed the listing
                if user != listing.owner:
                    raise KeyError

                else:
                    if request.POST["close"]:

                        # Close the listing
                        listing.closed = True

                        # Update the listing
                        listing.save()

            except KeyError:

                # Try to call bid via post, if error gets raised, a comment has been placed
                try:

                    # Get bidded value
                    bid = int(request.POST["bid"])

                    # Make bid object
                    bidding = Bid(bidder=user, value=bid, location=listing)

                    # Check if bidding is correct value
                    if bidding.value < listing.starting_bid:

                        # Get all comments from listing
                        comments = listing.location.all()

                        return render(request, "auctions/listing.html", {
                            "listing" : listing,
                            "error" : "Bid is too low !",
                            "in_watchlist" : in_watchlist,
                            "comments" : comments,
                            "closed" : listing.closed
                        })

                    # Save bid object
                    bidding.save()

                    # Change the value of the bid
                    listing.starting_bid = bidding.value

                    # Set highest bidder to new user
                    listing.highest_bidder = user

                    # Update the listing
                    listing.save()

                except KeyError:

                    # Comment has been placed
                    # Get comment
                    comment_text = request.POST["comment"]

                    # Create comment and save it to database
                    comment = Comment(author=user, text=comment_text, location=listing)
                    comment.save()

    # Get all comments from listing
    comments = listing.location.all()

    return render(request, "auctions/listing.html", {
        "listing" : listing,
        "error" : None,
        "in_watchlist" : in_watchlist,
        "comments" : comments,
        "closed" : listing.closed
    })


@login_required
def watch(request):

    # Get the user
    user = User.objects.get(username=request.user.username)

    # Get user's listings from his watchlist if any
    all_listings = user.watchlist.all()

    return render(request, "auctions/watch.html", {
        "watchlist" : all_listings
    })


def categories(request):
    return render(request, "auctions/categories.html", {
        "categories" : Listing.CATEGORY_CHOICES
    })
