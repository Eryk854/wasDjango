# Generated by Django 3.0 on 2019-12-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='sum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]