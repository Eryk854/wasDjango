# Generated by Django 3.0 on 2019-12-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0009_auto_20191220_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
    ]
