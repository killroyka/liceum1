from django.shortcuts import render


def item_list(request):
    return render(request, "catalog/list.html")


def item_detail(request, id):
    return render(request, "catalog/detail.html")
