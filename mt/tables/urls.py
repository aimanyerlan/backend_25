from django.urls import path
from . import views

urlpatterns = [
    path('', views.tables_list, name='tables_list'),  
    path('create/', views.create_table, name='create_table'),  
    path('available/', views.available_tables, name='available_tables'),  
]
