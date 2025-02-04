# from django.contrib import admin
from django.urls import path
from blog.views import index, article

urlpatterns = [
    path('', index, name='index'),
    path('<int:article_id>/', article, name='article'),
]
