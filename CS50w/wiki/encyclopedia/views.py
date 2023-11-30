from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

# Get list of all names of wiki pages
entries = util.list_entries()

search_reqeust = None

def index(request):

    # Check if user submitted a search request
    if request.method == "POST":

        # Get the search submitted by the user
        search_req = request.POST["q"]
        global search_request
        print(search_request)

        # Check if search is in the list of entries, if so redirect to given search
        if search_req in entries:

            # Redirect users
            return HttpResponseRedirect(reverse(entry, args=[search_req]))
        else:

            # Redirect user to search page
            return HttpResponseRedirect(reverse(search))


    # Return the home page
    return render(request, "encyclopedia/index.html", {
        "entries": entries,
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
    })


def search(request):


    return render(request, "encyclopedia/search.html")
