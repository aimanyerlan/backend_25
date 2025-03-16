from django.urls import path
from .views import notes_list, note_detail, note_delete, note_create, note_edit

urlpatterns = [
    path('', notes_list, name='notes_list'),
    path('<int:id>/', note_detail, name='note_detail'),
    path('<int:id>/delete/', note_delete, name='note_delete'),
    path('create/', note_create, name='note_create'),
    path('<int:id>/edit/', note_edit, name='note_edit'),
]
