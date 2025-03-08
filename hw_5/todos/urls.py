from django.urls import path
from .views import todos_list, todo_detail, todo_new_status, delete_todo

urlpatterns = [
    path('todos/', todos_list, name='todos_list'),
    path('todos/<int:todo_id>/', todo_detail, name='todo_detail'),
    path('todos/<int:todo_id>/new-status/', todo_new_status, name='todo_new_status'),
    path('todos/<int:todo_id>/delete/', delete_todo, name='delete_todo'),
]
