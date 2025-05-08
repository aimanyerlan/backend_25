from django.urls import path
from .views import post_detail, post_list, comment_detail, comment_list

urlpatterns = [
    path('posts/', post_list),
    path('posts/<int:pk>/', post_detail),
    path('posts/<int:post_id>/comments/', comment_list),
    path('posts/<int:post_id>/comments/<int:comment_id>/', comment_detail),
]
