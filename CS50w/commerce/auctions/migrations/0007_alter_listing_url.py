# Generated by Django 4.2.7 on 2023-12-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0006_alter_listing_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="url",
            field=models.CharField(max_length=1024),
        ),
    ]
