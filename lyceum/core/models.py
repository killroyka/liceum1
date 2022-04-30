from django.db import models

from catalog.validators import validate_eng


class IsPublishedSlug(models.Model):
    is_published = models.BooleanField(verbose_name="Опубликовано", default=True)
    slug = models.CharField(verbose_name="Жетон", max_length=200, validators=[validate_eng], unique=True, blank=True)

    class Meta:
        abstract = True
