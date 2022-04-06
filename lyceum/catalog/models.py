from django.db import models
from .validators import validate_brilliant, validate_max_number
from core.models import IsPublishedSlug
from random import randint


class ItemManager(models.Manager):
    def get_random_items(self, count=3):
        items = Item.objects.filter(is_published=True).prefetch_related("tag").only("name", "text", "tag")
        if len(items) > count:
            indexes = []
            rand_items = []
            while len(indexes) != count:
                randint_ = randint(0, len(items) - 1)
                if randint_ not in indexes:
                    indexes.append(randint_)
                    rand_items.append(items[randint_])
            return rand_items
        return items


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


class Item(IsPublishedSlug):
    slug = None
    name = models.CharField(verbose_name="Название", max_length=150, blank=True)
    text = models.TextField(verbose_name="Описание", validators=[validate_brilliant], null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.DO_NOTHING, default=None,
                                 null=True)
    tag = models.ManyToManyField(Tag, verbose_name="Тэг", null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    objects = ItemManager()
