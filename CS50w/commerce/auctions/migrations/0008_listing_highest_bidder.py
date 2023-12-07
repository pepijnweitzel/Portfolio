# Generated by Django 4.2.7 on 2023-12-07 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0007_alter_listing_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="highest_bidder",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]