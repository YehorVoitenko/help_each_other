from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('registration', views.register, name='register'),
    path('registration/welldone', views.warning, name='warning'),
    path('index', views.index, name='index'),
]