from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index),
    path("products/",views.product_list, name="product_list"),
    path("products/<int:product_id>", views.product_details, name='product_details'),
    path("products/add_comment/",views.add_comment),
    path("products/vote/", views.vote),
    path("order/<int:order_id>", views.order_details),
    path("order/", views.order),
    path("complaint/", views.complaint),
    path("complaint/<int:complaint_id>",views.complaint_details, name="complaint_details"),
    path("cart/",views.cart),
    path("cart/add/",views.add_to_cart),
    path("cart/delete/<str:product_id>",views.delete_item)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)