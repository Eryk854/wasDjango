# Generated by Django 2.2.7 on 2019-12-05 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklep.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sklep.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='sklep.OrderedProducts', to='sklep.Product'),
        ),
    ]
