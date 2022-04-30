from django.urls import path

from . import views

urlpatterns = [
    path("", views.ItemListView.as_view(), name="item_list"),
    path("<int:id>/",  views.ItemDetailView.as_view(), name="item_detail"),
]
