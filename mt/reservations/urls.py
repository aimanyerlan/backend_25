from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list_create, name='reservations_list'),
    path('create/', views.create_reservation, name='create_reservation'), 
    path('<int:id>/', views.reservation_detail, name='reservation_detail'),
    path('user/<int:user_id>/', views.user_reservations, name='user_reservations'),
    path('<int:id>/update/', views.update_reservation_status, name='update_reservation_status'),
    path('<int:id>/delete/', views.delete_reservation, name='delete_reservation'),
]
