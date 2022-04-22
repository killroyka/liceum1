from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("<int:id>/", views.item_detail, name="item_detail"),
]
