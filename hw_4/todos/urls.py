from django.urls import path
from .views import todo_lists, todo_list_detail, todo_list_edit, todo_list_delete, todo_edit, todo_delete

urlpatterns = [
    path('todo-lists/', todo_lists, name='todo_lists'),
    path('todo-lists/<int:id>/', todo_list_detail, name='todo_list_detail'),
    path('todo-lists/<int:id>/edit/', todo_list_edit, name='todo_list_edit'),
    path('todo-lists/<int:id>/delete/', todo_list_delete, name='todo_list_delete'),
    path('todos/<int:id>/edit/', todo_edit, name='todo_edit'),
    path('todos/<int:id>/delete/', todo_delete, name='todo_delete'),
]



