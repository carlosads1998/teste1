from django.urls import path
from . import views

urlpatterns = [
    path('publi/', views.publiApi.as_view(), name='Publicação'),
    path('publi/<int:user>/', views.publiView.as_view(), name='Publicações'),
]
