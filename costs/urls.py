from django.urls import path
from costs import views

app_name = 'costs'

urlpatterns = [
    path('costs_form', views.costs_form, name='costs_form'),

    path('costs_list', views.costs_list, name='costs_list'),

    path('costs_details/<int:id>', views.costs_details, name='costs_details'),

    path('costs_delete/<int:id>', views.costs_delete, name='costs_delete'),
]