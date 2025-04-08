from django.urls import path
from bellafral import views

app_name = 'bellafral'

urlpatterns = [
    path('bellafral_form', views.bellafral_form, name='bellafral_form'),

    path('bellafral_list', views.bellafral_list, name='bellafral_list'),

    path('bellafral_details/<int:id>', views.bellafral_details, name='bellafral_details'),

    path('bellafral_pre_simulator', views.bellafral_pre_simulator, name='bellafral_pre_simulator'),

    path('bellafral_simulator', views.bellafral_simulator, name='bellafral_simulator'),

    path('download_simulation', views.download_simulation, name='download_simulation'),
]