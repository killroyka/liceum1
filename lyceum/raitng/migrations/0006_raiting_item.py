# Generated by Django 3.2 on 2022-03-23 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20220323_0614'),
        ('raitng', '0005_alter_raiting_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='raiting',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.item'),
        ),
    ]