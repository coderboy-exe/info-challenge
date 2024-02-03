from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.article, name='article'),
    path('providers/', views.provider, name='providers'),
    path('prices/', views.price, name='prices'),
]