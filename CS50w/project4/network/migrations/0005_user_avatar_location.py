# Generated by Django 5.0 on 2024-01-15 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_user_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_location',
            field=models.CharField(default='/static/network/avatars/avatar1.png', max_length=255),
        ),
    ]
