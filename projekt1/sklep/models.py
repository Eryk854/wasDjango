from django.db import models


# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    price = models.FloatField(default = 0)
    description = models.CharField(max_length=500, default='Brak opisu')
    weight = models.FloatField(default=0)

class Order(models.Model):
    def __str__(self):
        return self.first_name +' '+ self.last_name

    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    address = models.CharField(max_length=100)
    delivery = models.CharField(max_length=30)
