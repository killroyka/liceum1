# Generated by Django 4.0.4 on 2022-04-30 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('raitng', '0001_initial'), ('raitng', '0002_alter_raiting_star'), ('raitng', '0003_alter_raiting_star'), ('raitng', '0004_raiting_user'), ('raitng', '0005_alter_raiting_options'), ('raitng', '0006_raiting_item'), ('raitng', '0007_remove_raiting_item'), ('raitng', '0008_auto_20220323_0630'), ('raitng', '0009_raiting_user'), ('raitng', '0010_raiting_unique_raiting'), ('raitng', '0011_auto_20220325_0855'), ('raitng', '0012_auto_20220326_1950'), ('raitng', '0013_auto_20220426_1816')]

    initial = True

    dependencies = [
        ('catalog', '0006_alter_category_weight'),
        ('catalog', '0005_auto_20220325_0855'),
        ('catalog', '0007_auto_20220426_1816'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0004_auto_20220323_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(choices=[('0', ''), ('1', 'Ненависть'), ('2', 'Неприязнь'), ('3', 'Нейтрально'), ('4', 'Обожание'), ('5', 'Любовь')], default=0, max_length=1)),
                ('item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.item')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
        migrations.AddConstraint(
            model_name='raiting',
            constraint=models.UniqueConstraint(fields=('user', 'item'), name='unique_raiting'),
        ),
        migrations.AlterField(
            model_name='raiting',
            name='item',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.item'),
        ),
        migrations.AlterField(
            model_name='raiting',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
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
        migrations.AlterField(
            model_name='raiting',
            name='item',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='raitings', to='catalog.item', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='raiting',
            name='star',
            field=models.CharField(choices=[('0', ''), ('1', 'Ненависть'), ('2', 'Неприязнь'), ('3', 'Нейтрально'), ('4', 'Обожание'), ('5', 'Любовь')], default='0', max_length=1, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='raiting',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='raitings', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
