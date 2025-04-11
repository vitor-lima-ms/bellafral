from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),

    path('simulator_edit/<int:id>/', views.simulator_edit, name='simulator_edit'),

    path('simulator_save/<int:id>/', views.simulator_save, name='simulator_save'),
]
