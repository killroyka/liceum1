from django.db import models
from django.db.models import Prefetch
from .validators import validate_brilliant, validate_max_number
from core.models import IsPublishedSlug
import random


class CategoryManager(models.Manager):
    def get_items_group_by_categories(self):
        categories = Category.objects.filter(is_published=True).prefetch_related(
            Prefetch("items", queryset=Item.objects.filter(is_published=True).prefetch_related(
                Prefetch("tag", queryset=Tag.objects.filter(is_published=True))))) \
            .order_by("weight")
        return categories


class ItemManager(models.Manager):
    def get_random_items(self, count=3):
        item = Item.objects.filter(
            id__in=random.sample(set(Item.objects.all().values_list('id', flat=True)), k=count)) \
            .prefetch_related("tag") \
            .only("name", "text", "tag")
        return item


class Tag(IsPublishedSlug):
    name = models.CharField(verbose_name="Название", max_length=150, blank=True)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Category(IsPublishedSlug):
    weight = models.DecimalField(verbose_name="Масса", default=100, decimal_places=0, max_digits=5,
                                 validators=[validate_max_number])
    name = models.CharField(verbose_name="Название", max_length=150, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    objects = CategoryManager()


class Item(IsPublishedSlug):
    slug = None
    name = models.CharField(verbose_name="Название", max_length=150, blank=True)
    text = models.TextField(verbose_name="Описание", validators=[validate_brilliant], null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", related_name='items',
                                 on_delete=models.DO_NOTHING, default=None,
                                 null=True)
    tag = models.ManyToManyField(Tag, verbose_name="Тэг", null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    objects = ItemManager()
