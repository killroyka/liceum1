# Generated by Django 3.2 on 2022-03-26 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_category_weight'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raitng', '0011_auto_20220325_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiting',
            name='item',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.item', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='raiting',
            name='star',
            field=models.CharField(choices=[('0', ''), ('1', 'Ненависть'), ('2', 'Неприязнь'), ('3', 'Нейтрально'), ('4', 'Обожание'), ('5', 'Любовь')], default=0, max_length=1, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='raiting',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
