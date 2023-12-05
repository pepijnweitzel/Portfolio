# Generated by Django 4.2.7 on 2023-12-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0003_alter_listing_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="listing",
            old_name="user",
            new_name="owner",
        ),
        migrations.AlterField(
            model_name="listing",
            name="url",
            field=models.CharField(
                default="https://www.google.com/url?sa=i&url=http%3A%2F%2Fbeepeers.com%2Fassets%2Fimages%2Fcommerces%2F&psig=AOvVaw0CXks0Pp84eKZkY5nVy9Q8&ust=1701875483635000&source=images&cd=vfe&ved=0CBIQjRxqFwoTCJj7vK_K-IIDFQAAAAAdAAAAABAE",
                max_length=1024,
            ),
        ),
    ]
