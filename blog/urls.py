from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostsList.as_view(), name='blog'),
    # path('', views.posts_list, name='blog'),
    path('<int:pk>/', views.show_detail, name='show_detail'),
    path('newpost/', views.NewPost.as_view(), name='new_post'),
    # path('newpost/', views.new_post, name='new_post'),
    path('update/<int:pk>/', views.UpdatePost.as_view(), name='update_post'),
    # path('update/<int:pk>/', views.update_post, name='update_post'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete_post'),
    # path('delete/<int:pk>/', views.delete_post, name='delete_post'),
]
