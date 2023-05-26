from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.UserApi.as_view(), name='register'),
    path('cadastro/<int:pk>', views.UserView.as_view(), name='register_'),
]
