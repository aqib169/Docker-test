from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:id>/', views.post_detail, name='post-detail'),
]
