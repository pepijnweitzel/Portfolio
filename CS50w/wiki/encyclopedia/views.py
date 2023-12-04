from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

import random

from . import util

# Create class for form
class NewPageForm(forms.Form):
    page_title = forms.CharField(label="Page Title", )


def index(request):

    # Get entries
    entries = util.list_entries()

    # Pick a random page
    random_page = [random.choice(entries)]

    # Check if user submitted a search request
    if request.method == "POST":

        # Get the search submitted by the user
        search_req = request.POST["q"]

        # Check if search is in the list of entries, if so redirect to given search
        if search_req in entries:

            # Redirect users
            return HttpResponseRedirect(reverse(entry, args=[search_req]))
        else:

            # Redirect user to search page
            return HttpResponseRedirect(reverse("search", args=[search_req]))

    # Return the home page
    return render(request, "encyclopedia/index.html", {
        "entries" : entries,
        "random" : random_page
    })


def entry(request, title):

    # Get entries
    entries = util.list_entries()

    # Pick a random page
    random_page = [random.choice(entries)]

    # Check if page exists
    if title in entries:
        entry_content = util.get_entry(title)
    else:
        # Make error message and sent it as input
        error_message = "Sorry, page does not exist"
        entry_content = error_message
    return render(request, "encyclopedia/entry.html", {
        "title" : title,
        "titles" : [title],
        "entry" : entry_content,
        "random" : random_page
    })


def search(request, input):

    # Create list to put search results in
    possible_entries = []

    # Get entries
    entries = util.list_entries()

    # Pick a random page
    random_page = [random.choice(entries)]

    # Iterate over all entries to check if it is substring of
    for title in entries:

        # Check if it is substring
        if input.lower() in title.lower():

            # Add title to the list of entries
            possible_entries.append(title)

    return render(request, "encyclopedia/search.html", {
        "titles" : possible_entries,
        "random" : random_page
    })


def new(request):

    # Get entries
    entries = util.list_entries()

    # Pick a random page
    random_page = [random.choice(entries)]

    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewPageForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            page_title = form.cleaned_data["page_title"]

            # Check if page already exists
            if page_title in entries:

                # If the form is invalid, re-render the page with existing information.
                return render(request, "encyclopedia/new.html", {
                    "title_form": form,
                    "placeholder" : "Page already exists",
                    "random" : random_page,
                })
            # If page does not already exist
            else:
                # Retrieve content for page
                page_content = f"# {page_title.capitalize()}\n\n{request.POST["page_content"]}\n"

                # Save the page
                util.save_entry(page_title, page_content)

                # Redirect user to new page
                return HttpResponseRedirect(reverse(entry, args=[page_title]))


    return render(request, "encyclopedia/new.html", {
        "title_form": NewPageForm(),
        "placeholder": "Page context",
        "random" : random_page,
    })


def edit(request, title):

    context = util.get_entry(title)

    return render(request, "encyclopedia/edit.html", {
        "title" : title,
        
    })
