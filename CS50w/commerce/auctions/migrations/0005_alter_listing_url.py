# Generated by Django 4.2.7 on 2023-12-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0004_rename_user_listing_owner_alter_listing_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="url",
            field=models.CharField(
                default="https://cdn.vectorstock.com/i/1000x1000/79/45/product-image-default-thumbnail-icon-graphic-web-vector-49027945.webp",
                max_length=1024,
            ),
        ),
    ]
