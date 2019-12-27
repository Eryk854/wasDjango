from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator,MinValueValidator,MaxValueValidator

# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    price = models.FloatField(default = 0)
    description = models.CharField(max_length=500, default='Brak opisu')
    weight = models.FloatField(default=0)
    votes = models.IntegerField(default=0)
    sum = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)


class Order(models.Model):
    def __str__(self):
        return self.first_name +' '+ self.last_name

    def get_total_prices(self):
        total = 0
        order_products = OrderedProducts.objects.filter(order=self)
        for order_product in order_products:
            total += order_product.amount * order_product.product.price
        return round(total,2)

    def total_price_with_discount(self):
        discount = self.discount_code.discount
        return round(self.get_total_prices()-self.get_total_prices()*discount, 2)

    def get_products(self):
        return OrderedProducts.objects.filter(order=self)

    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    address = models.CharField(max_length=100)
    delivery = models.CharField(max_length=30)
    products = models.ManyToManyField("Product", through="OrderedProducts")
    discount_code = models.ForeignKey("Discount", on_delete=models.PROTECT, blank=True, null=True)


class OrderedProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)


class Comments(models.Model):
    text = models.CharField(max_length=220)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Complaint(models.Model):
    name = models.CharField(max_length=70)
    message = models.CharField(max_length=120)

class Discount(models.Model):
    code = models.CharField(validators=[MinLengthValidator(8)], max_length=8)
    discount = models.FloatField(validators=[MaxValueValidator(1.0), MinValueValidator(0.0)])
