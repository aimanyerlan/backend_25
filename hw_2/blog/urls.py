from django.urls import path
from .views import article_list, article_create

urlpatterns = [
    path('', article_list, name='article-list'),
    path('create/', article_create, name='article-create'),
]
