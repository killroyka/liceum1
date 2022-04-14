from django.conf import settings
from django.db import models
from catalog.models import Item


class Raiting(models.Model):
    STAR_CHOICES = [
        ('0', ''),
        ('1', 'Ненависть'),
        ('2', 'Неприязнь'),
        ('3', 'Нейтрально'),
        ('4', 'Обожание'),
        ('5', 'Любовь'),
    ]
    star = models.CharField(verbose_name="Оценка", choices=STAR_CHOICES, default=0, max_length=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', related_name="raitings",
                             on_delete=models.CASCADE,
                             blank=True)
    item = models.ForeignKey(Item, verbose_name='Товар', on_delete=models.CASCADE, default=None, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(name='unique_raiting', fields=['user', 'item']),
        ]
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
