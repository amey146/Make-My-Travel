# Generated by Django 4.2.2 on 2023-08-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_itinerary_itineraryday'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itinerary',
            options={'verbose_name_plural': 'Itineraries'},
        ),
        migrations.AlterField(
            model_name='itineraryday',
            name='Description',
            field=models.CharField(max_length=250),
        ),
    ]