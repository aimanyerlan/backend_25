from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_thread, name='index_thread'),
    path('threads/<int:thread_id>/', views.thread_details, name='thread_details'),
    path('threads/<int:thread_id>/edit/', views.update_thread, name='update_thread'),
    path('threads/<int:thread_id>/delete/', views.delete_thread, name='delete_thread'),
    path('posts/<int:thread_id>/<int:post_id>/edit/', views.update_post, name='update_post'),
    path('posts/<int:thread_id>/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
