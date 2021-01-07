from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("new-entry", views.Entry_Form, name="Entry_Form"),
    path("random", views.random_page, name="random"),
    path("search", views.search_entry, name="search"),
    path("edit/<str:entry>", views.edit_entry, name="edit"),
]
