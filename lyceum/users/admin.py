from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Birthday


class BirthdayInlined(admin.TabularInline):
    model = Birthday
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (BirthdayInlined,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
