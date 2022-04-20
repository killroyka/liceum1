from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.shortcuts import get_object_or_404
from catalog.models import Item
from .forms import UserForm, BirthdayForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


def signup(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        # login(request, new_user)
        return redirect("profile")
    return render(request, "users/signup.html", {"form": form})


@login_required
def profile(request):
    user_form = UserForm(request.POST or None,
                         initial={"email": request.user.email, "first_name": request.user.first_name,
                                  "last_name": request.user.last_name})
    birthday_form = BirthdayForm(request.POST or None, initial={"birthday": request.user.birthday.birthday})
    if user_form.is_valid() and birthday_form.is_valid():
        print(user_form.cleaned_data)
        request.user.email = user_form.cleaned_data["email"]
        request.user.first_name = user_form.cleaned_data["first_name"]
        request.user.last_name = user_form.cleaned_data["last_name"]
        request.user.birthday.birthday = birthday_form.cleaned_data["birthday"]
        request.user.birthday.save(update_fields=["birthday"])
        request.user.save(update_fields=["email", "first_name", "last_name"])
        return redirect("profile")
    return render(request, "users/profile.html", {"user_form": user_form, "birthday_form": birthday_form})


def user_list(request):
    users = User.objects.all().prefetch_related("birthday")
    return render(request, "users/user_list.html", {"users": users})


def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    favorite_items = Item.objects \
        .prefetch_related("raitings") \
        .filter(raitings__user__id=id) \
        .filter(raitings__star="5")
    # for x in favorite_items:
    #     for y in x.raitings:
    #         print(y)
    return render(request, "users/user_detail.html", {"user": user, "favorite_items": (favorite_items)})
