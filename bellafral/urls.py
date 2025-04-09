from django.urls import path
from bellafral import views

app_name = 'bellafral'

urlpatterns = [
    path('bellafral_form', views.bellafral_form, name='bellafral_form'),

    path('bellafral_list', views.bellafral_list, name='bellafral_list'),

    path('bellafral_details/<int:id>', views.bellafral_details, name='bellafral_details'),

    path('bellafral_delete/<int:id>', views.bellafral_delete, name='bellafral_delete'),

    path('bellafral_edit/<int:id>', views.bellafral_edit, name='bellafral_edit'),

    path('bellafral_edit_save/<int:id>', views.bellafral_edit_save, name='bellafral_edit_save'),

    path('bellafral_pre_simulator', views.bellafral_pre_simulator, name='bellafral_pre_simulator'),

    path('bellafral_simulator', views.bellafral_simulator, name='bellafral_simulator'),

    path('download_simulation/<int:id>', views.download_simulation, name='download_simulation'),

    path('simulator_list', views.simulator_list, name='simulator_list'),

    path('simulator_details/<int:id>', views.simulator_details, name='simulator_details'),

    path('simulator_delete/<int:id>', views.simulator_delete, name='simulator_delete'),
]