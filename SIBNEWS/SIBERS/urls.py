from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('donate/', views.donation, name='donation')
]
