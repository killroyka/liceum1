from django.db import models
from catalog.validators import validate_brilliant, validate_eng, validate_max_number


class Slug(models.Model):
    slug = models.CharField(verbose_name="Жетон", max_length=200, validators=[validate_eng], unique=True)

    class Meta:
        abstract = True


class IsPublished(models.Model):
    is_published = models.BooleanField(verbose_name="Опубликовано", default=True)

    class Meta:
        abstract = True
