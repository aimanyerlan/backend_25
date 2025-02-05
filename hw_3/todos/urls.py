from django.urls import path
from .views import index, todo_detail, todo_delete, todo_create, todo_new_status

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', todo_detail, name='todo_detail'),
    path('create/', todo_create, name='todo_create'),
    path('<int:id>/delete/', todo_delete, name='todo_delete'),
    path('<int:id>/new-status/', todo_new_status, name='todo_new_status'),
]
