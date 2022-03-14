from django.shortcuts import render
from django.http import HttpResponse


def user_list(request):
    return HttpResponse("Список пользователей")


def user_detail(requests, id):
    return HttpResponse(f"Информация о пользователе {id}")


def signup(request):
    return HttpResponse("Регистрация")


def profile(request):
    return HttpResponse("Мой профиль")
