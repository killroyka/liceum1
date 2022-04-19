from django.shortcuts import render
from catalog.models import Item
from django.core.mail import send_mail


def home(request):
    send_mail("dla", "dka", "from@example.ru", ["to@example.ru"])
    items = Item.objects.get_random_items()
    return render(request, "homepage/home.html", {'items': items})
