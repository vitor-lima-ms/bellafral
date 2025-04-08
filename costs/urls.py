from django.urls import path
from costs import views

app_name = 'costs'

urlpatterns = [
    path('costs_form', views.costs_form, name='costs_form'),
]