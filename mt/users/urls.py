from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list_create, name='users_list'),  # Чтобы URL users/ срабатывал на users_list_create
    path('<int:id>/', views.user_detail, name='user_detail'),  # Для получения пользователя по id
]
