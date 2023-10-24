from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts_list, name='blog'),
    path('<int:pk>/', views.show_detail, name='show_detail'),
    path('newpost/', views.new_post, name='new_post'),
]
