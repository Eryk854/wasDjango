# Generated by Django 3.0 on 2019-12-20 13:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0006_auto_20191220_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8)])),
                ('discount', models.FloatField(validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
    ]
