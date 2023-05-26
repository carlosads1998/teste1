from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.postView.as_view(), name='feed'),
    path('posts/<int:pk>', views.postView.as_view(), name='feed'),
]
