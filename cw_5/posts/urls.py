from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.posts_list, name="posts_list"),
    path("posts/my/", views.my_posts, name="my_posts"),
    path("posts/<int:id>/", views.post_detail, name="post_detail"),
    path("posts/new/", views.create_post, name="create_post"),
    path("posts/<int:id>/edit/", views.update_post, name="update_post"),
    path("posts/<int:id>/delete/", views.delete_post, name="delete_post"),
]
