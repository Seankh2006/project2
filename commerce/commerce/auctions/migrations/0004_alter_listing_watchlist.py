# Generated by Django 4.1.7 on 2023-05-30 11:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='watchlist2', to=settings.AUTH_USER_MODEL),
        ),
    ]
