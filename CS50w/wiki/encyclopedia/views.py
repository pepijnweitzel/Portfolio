from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

for entry in util.list_entries():
    entrypage = f"{entry}page"
    def entrypage(request):
        return render(request, f"encyclopedia/{entry}")
