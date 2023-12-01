from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

# Get list of all names of wiki pages
entries = util.list_entries()

# Create class for form
class NewPageForm(forms.Form):
    page_title = forms.CharField(label="Page Title", )


def index(request):

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
        "entries": entries,
    })


def entry(request, title):

    # Check if page exists
    if title in entries:
        entry_content = util.get_entry(title)
    else:
        # Make error message and sent it as input
        error_message = "Sorry, page does not exist"
        entry_content = error_message
    return render(request, "encyclopedia/entry.html", {
        "title" : title,
        "entry" : entry_content,
    })


def search(request, input):

    # Create list to put search results in
    possible_entries = []

    # Iterate over all entries to check if it is substring of
    for title in entries:

        # Check if it is substring
        if input.lower() in title.lower():

            # Add title to the list of entries
            possible_entries.append(title)

    return render(request, "encyclopedia/search.html", {
        "titles" : possible_entries
    })


def new(request):

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
                    "placeholder" : "Page already exists"
                })
            # If page does not already exist
            else:
                # Retrieve content for page
                page_content = request.POST["page_content"]

                # Save the page
                util.save_entry(page_title, page_content)

                # Redirect user to new page
                return HttpResponseRedirect(reverse(entry, args=[page_title]))


    return render(request, "encyclopedia/new.html", {
        "title_form": NewPageForm(),
        "placeholder": "Page context"
    })
