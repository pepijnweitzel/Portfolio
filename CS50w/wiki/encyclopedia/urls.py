from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("<str:input>", views.search, name="search"),
    path("page/new", views.new, name="new")
]
