# Generated by Django 4.2.7 on 2023-12-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0005_alter_listing_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="url",
            field=models.CharField(
                default="https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png",
                max_length=1024,
            ),
        ),
    ]