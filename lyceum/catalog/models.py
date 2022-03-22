import decimal

from django.db import models
from .validators import validate_brilliant, validate_eng, validate_max_number
from core.models import Slug, IsPublished


class Tag(IsPublished, Slug):
    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Category(IsPublished, Slug):
    weight = models.DecimalField(default=100, decimal_places=0, max_digits=5, validators=[validate_max_number])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Item(IsPublished):
    name = models.CharField(verbose_name="Название", max_length=150)
    text = models.TextField(verbose_name="Описание", validators=[validate_brilliant])
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.DO_NOTHING, default=None)
    tag = models.ManyToManyField(Tag, verbose_name="Тэг")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
