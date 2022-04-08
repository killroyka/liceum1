from django.shortcuts import render
from catalog.models import Item
from django.shortcuts import get_object_or_404


def item_list(request):
    items = Item.objects.get_random_items()
    return render(request, "catalog/list.html", {'items': items})


def item_detail(request, id):
    item = get_object_or_404(Item, pk=id, is_published=True)
    return render(request, "catalog/detail.html", {"items": [item]})
