from django.db import models
from django.contrib.auth.models import User

class Raiting(models.Model):
    STAR_CHOICES=[
        ('0', ''),
        ('1', 'Ненависть'),
        ('2', 'Неприязнь'),
        ('3', 'Нейтрально'),
        ('4', 'Обожание'),
        ('5', 'Любовь'),
    ]
    star = models.CharField(choices=STAR_CHOICES, default=0, max_length=1)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
