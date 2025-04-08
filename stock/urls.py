from django.urls import path
from stock import views

app_name = 'stock'

urlpatterns = [
    path('stock_form', views.stock_form, name='stock_form'),
]