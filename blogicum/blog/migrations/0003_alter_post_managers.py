# Generated by Django 3.2.16 on 2024-07-16 18:16

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240716_2012'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('main_filter', django.db.models.manager.Manager()),
            ],
        ),
    ]
