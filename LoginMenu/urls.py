from . import views
from django.urls import path


urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('homepage/', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.logIn, name='login'),
]
