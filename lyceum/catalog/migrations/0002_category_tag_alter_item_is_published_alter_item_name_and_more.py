# Generated by Django 4.0.3 on 2022-03-21 09:57

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.CharField(max_length=200, validators=[catalog.validators.validate_eng])),
                ('weight', models.DecimalField(decimal_places=0, default=100, max_digits=5, validators=[catalog.validators.validate_max_number])),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.CharField(max_length=200, validators=[catalog.validators.validate_eng])),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(validators=[catalog.validators.validate_brilliant]),
        ),
    ]
