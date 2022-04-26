from django.contrib import admin
from .models import Item, Tag, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published', 'image_tmb']
    list_editable = ['is_published']
    filter_horizontal = ['tag']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
