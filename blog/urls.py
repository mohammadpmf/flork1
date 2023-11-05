from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts_list, name='blog'),
    path('<int:pk>/', views.show_detail, name='show_detail'),
    path('newpost/', views.new_post, name='new_post'),
    path('update/<int:pk>/', views.update_post, name='update_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
]
