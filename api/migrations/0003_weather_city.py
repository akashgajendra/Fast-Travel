# Generated by Django 4.0.5 on 2022-06-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_weather'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='city',
            field=models.CharField(default='', max_length=60),
        ),
    ]