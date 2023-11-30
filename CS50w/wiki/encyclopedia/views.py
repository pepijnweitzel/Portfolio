from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

# Create class for search results
class NewSearchForm(forms.Form):
    search_req = forms.CharField()

# Get list of all names of wiki pages
entries = util.list_entries()


def index(request):

    # Check if user submitted a search request
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewSearchForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the search from the 'cleaned' version of form data
            search = form.cleaned_data["q"]
            print(search)
        else:
            print("noooo")

    # Return the home page
    return render(request, "encyclopedia/index.html", {
        "entries": entries,
        "form": NewSearchForm()
    })


def entry(request, title):

    # Check if page exists
    if title in entries:
        entry_content = util.get_entry(title)
    else:
        # Make error message and sent it as input
        error_message = "Sorry, page does not exist yet"
        entry_content = error_message
    return render(request, "encyclopedia/entry.html", {
        "title" : title,
        "entry" : entry_content,
        "form": NewSearchForm()
    })

