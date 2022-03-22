from django.contrib import admin
from .models import Raiting


@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    pass
