from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Birthday(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', related_name="birthday", on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "День рождения"
        verbose_name_plural = "Дни рождения"

    @receiver(post_save, sender=User)
    def create_or_update_user_birthday(sender, instance, created, **kwargs):
        if created:
            Birthday.objects.create(user=instance)
        instance.birthday.save()
