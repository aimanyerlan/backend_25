# from django.urls import path
# from .views import index, post_details, post_delete

# urlpatterns = [
#     path('', index, name='post_list'),
#     path('<int:id>/', post_details, name='post_details'),
#     path('<int:id>/delete', post_delete, name='post_delete'),
# ]

from django.urls import path
from .views import index, post_details, post_create, post_delete

urlpatterns = [
    path('', index, name='post_list'),
    path('<int:id>/', post_details, name='post_detail'),
    path('create/', post_create, name='post_create'),  
    path('<int:id>/delete/', post_delete, name='post_delete'),
]
