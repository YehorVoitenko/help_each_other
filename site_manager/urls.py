from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('user', views.give_help, name='give_help'),
]