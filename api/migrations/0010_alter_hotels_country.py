# Generated by Django 4.0.5 on 2022-07-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_hotels_country_alter_hotels_hotel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='country',
            field=models.CharField(default='', max_length=200),
        ),
    ]
