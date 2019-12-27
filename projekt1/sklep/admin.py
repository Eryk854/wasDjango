from django.contrib import admin
from .models import Product, Order, OrderedProducts, Complaint, Comments,Discount
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name')


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'order')


class CommentAdmin(admin.ModelAdmin):
    list_display=('text','product')


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Product)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderedProducts,OrderProductAdmin)
admin.site.register(Complaint)
admin.site.register(Comments,CommentAdmin)
admin.site.register(Discount,DiscountAdmin)


