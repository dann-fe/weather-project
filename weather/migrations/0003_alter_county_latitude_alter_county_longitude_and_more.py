# Generated by Django 5.1.4 on 2025-01-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_weather_latitude_weather_longitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='county',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='weather',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='weather',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='weather',
            name='temperature',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
