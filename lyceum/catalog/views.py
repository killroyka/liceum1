from django.shortcuts import render
from catalog.models import Item, Category
from django.shortcuts import get_object_or_404


def item_list(request):
    orderred_by_category = Item.objects.get_ordered_by_category()
    return render(request, "catalog/list.html", {"categories": orderred_by_category})


def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, "catalog/detail.html", {"items": [item]})
