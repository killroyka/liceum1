# Generated by Django 3.2 on 2022-03-26 19:50

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20220325_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.DecimalField(decimal_places=0, default=100, max_digits=5, validators=[catalog.validators.validate_max_number], verbose_name='Масса'),
        ),
    ]
