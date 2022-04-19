from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import get_object_or_404
from catalog.models import Item
from raitng.models import Raiting
from django.db.models import Prefetch


def signup(request):
    return render(request, "users/signup.html")


def profile(request):
    return render(request, "users/profile.html")


def user_list(request):
    users = User.objects.all().prefetch_related("birthday")
    return render(request, "users/user_list.html", {"users": users})


def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    favorite_items = Item.objects \
        .prefetch_related(
        Prefetch("raitings", queryset=Raiting.objects.prefetch_related("user").filter(user__id=id).only("star"))).filter(raitings__star="5")
    for x in favorite_items:
        print(x.raitings)
    return render(request, "users/user_detail.html", {"user": user})
