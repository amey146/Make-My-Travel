# Generated by Django 4.2.2 on 2023-08-31 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_places_alter_itinerary_offerprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='places',
            old_name='place',
            new_name='placename',
        ),
    ]
