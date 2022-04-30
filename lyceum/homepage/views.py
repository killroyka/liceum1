from catalog.models import Item
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "homepage/home.html"

    def get_context_data(self, **kwargs):
        send_mail("dla", "dka", "from@example.ru", ["to@example.ru"])
        items = Item.objects.get_random_items()
        return {'items': items}
