from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('registration', views.register, name='register'),
    path('registration/welldone', views.warning, name='warning'),
    path('registration/error', views.error, name='error'),
    path('registration/home_page', views.error, name='error'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

