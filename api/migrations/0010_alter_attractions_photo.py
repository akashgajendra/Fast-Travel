# Generated by Django 4.0.5 on 2022-07-12 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_attractions_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractions',
            name='photo',
            field=models.CharField(default='', max_length=600),
        ),
    ]
