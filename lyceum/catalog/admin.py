from django.contrib import admin

from .models import Category, Gallery, Item, Tag


class GalleryInlined(admin.StackedInline):
    model = Gallery
    can_delete = False

    class Meta:
        verbose_name = "Галлереи"
        verbose_name_plural = "Галлерея"


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published', 'image_tmb']
    list_editable = ['is_published']
    filter_horizontal = ['tag']
    inlines = [GalleryInlined, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
