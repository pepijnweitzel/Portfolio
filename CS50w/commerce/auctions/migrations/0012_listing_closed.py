# Generated by Django 4.2.7 on 2023-12-08 11:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0011_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="closed",
            field=models.BooleanField(default=False),
        ),
    ]