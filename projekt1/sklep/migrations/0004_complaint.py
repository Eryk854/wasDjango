# Generated by Django 2.2.7 on 2019-12-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0003_auto_20191205_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('message', models.CharField(max_length=120)),
            ],
        ),
    ]