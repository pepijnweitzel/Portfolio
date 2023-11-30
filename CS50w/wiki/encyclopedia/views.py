from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

# Get list of all names of wiki pages
entries = util.list_entries()


def index(request):

    # Check if user submitted a search request
    if request.method == "POST":

        print(request.post)

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

