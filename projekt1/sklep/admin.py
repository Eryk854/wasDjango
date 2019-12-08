from django.contrib import admin
from .models import Product, Order, OrderedProducts, Complaint
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name')

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'order')

admin.site.register(Product)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderedProducts,OrderProductAdmin)
admin.site.register(Complaint)


