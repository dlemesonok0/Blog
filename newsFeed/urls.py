from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='signup'),
    path('myposts/', views.user_posts, name='user_posts'),
    path('add/', views.add_post, name='add'),
    path('edit/<int:post_id>/', views.edit_post, name='edit'),
]