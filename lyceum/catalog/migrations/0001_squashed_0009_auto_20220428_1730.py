# Generated by Django 4.0.4 on 2022-04-30 16:13

import catalog.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('catalog', '0001_initial'), ('catalog', '0002_category_tag_alter_item_is_published_alter_item_name_and_more'), ('catalog', '0003_auto_20220322_0553'), ('catalog', '0004_auto_20220323_0614'), ('catalog', '0005_auto_20220325_0855'), ('catalog', '0006_alter_category_weight'), ('catalog', '0007_auto_20220426_1816'), ('catalog', '0008_gallery'), ('catalog', '0009_auto_20220428_1730')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.CharField(blank=True, max_length=200, unique=True, validators=[catalog.validators.validate_eng], verbose_name='Жетон')),
                ('weight', models.DecimalField(decimal_places=0, default=100, max_digits=5, validators=[catalog.validators.validate_max_number], verbose_name='Масса')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.CharField(blank=True, max_length=200, unique=True, validators=[catalog.validators.validate_eng], verbose_name='Жетон')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Название')),
                ('text', models.TextField(null=True, validators=[catalog.validators.validate_brilliant], verbose_name='Описание')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='catalog.category', verbose_name='Категория')),
                ('tag', models.ManyToManyField(null=True, to='catalog.tag', verbose_name='Тэг')),
                ('upload', models.ImageField(null=True, upload_to='uploads/')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(null=True, upload_to='uploads/')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='catalog.item')),
            ],
        ),
    ]
