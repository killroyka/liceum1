# Generated by Django 3.2 on 2022-03-22 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raitng', '0003_alter_raiting_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='raiting',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]