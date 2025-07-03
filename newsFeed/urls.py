from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='signup'),
    path('myposts/', views.user_posts, name='user_posts'),
    path('add/', views.add_post, name='add'),
    path('edit/<int:post_id>/', views.edit_post, name='edit'),
    path('details/<int:post_id>/', views.post_details, name='details'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
]