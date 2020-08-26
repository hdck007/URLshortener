from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUrl, name='getUrl'),
    path('<int:pk>/', views.handleUrl, name='handle'),
]