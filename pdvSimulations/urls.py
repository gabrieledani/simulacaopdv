from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulations, name='simulations'),
    path('delete_simulation/<simulation_id>', views.delete_simulation, name='delete_simulation'),
    path('edit_simulation/<simulation_id>', views.edit_simulation, name='edit_simulation'),
    path('simulation_items/<simulation_id>', views.simulation_items, name='simulation_items'),
    path('delete_items/<item_id>', views.delete_items, name='delete_items'),
    path('edit_items/<item_id>', views.edit_items, name='edit_items'),
]
