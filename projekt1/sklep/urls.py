from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path("widok/<str:tekst>", views.index),
    path("glowna/<str:tekst>", views.index1),
    path("products/",views.product_list),
    path("products/<int:product_id>",views.product_details)
]