from django.shortcuts import render
from catalog.models import Item, Category
from django.shortcuts import get_object_or_404


def item_list(request):
    categories = Category.objects.get_items_group_by_categories()
    return render(request, "catalog/list.html", {'categories': categories})


def item_detail(request, id):
    item = get_object_or_404(Item, pk=id, is_published=True)
    return render(request, "catalog/detail.html", {"items": [item]})
