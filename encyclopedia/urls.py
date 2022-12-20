from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.search_result, name="search"),
    path("wiki/<str:title>", views.entry, name="entry"),

    #needed to silent an error when entry doesn't exist:
    path("favicon.ico", views.index, name="favicon")
]