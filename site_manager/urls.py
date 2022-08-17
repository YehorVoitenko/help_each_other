from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('user', views.give_help, name='give_help'),
    path('help', views.receive_help, name='receive_help'),
    path('base', views.base, name='base'),
]