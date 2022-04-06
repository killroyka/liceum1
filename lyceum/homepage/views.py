from django.shortcuts import render
from catalog.models import Item
from random import randint



def home(request):
    items = Item.objects.get_random_items()
    return render(request, "homepage/home.html", {'items': items})
