from django.urls import path
from costs import views

app_name = 'costs'

urlpatterns = [
    path('costs_base', views.costs_base, name='costs_base'),

    path('costs_base_edit/<int:id>', views.costs_base_edit, name='costs_base_edit'),

    path('costs_base_save/<int:id>', views.costs_base_save, name='costs_base_save'),

    path('costs_form', views.costs_form, name='costs_form'),

    path('costs_list', views.costs_list, name='costs_list'),

    path('costs_details/<int:id>', views.costs_details, name='costs_details'),

    path('costs_delete/<int:id>', views.costs_delete, name='costs_delete'),
]