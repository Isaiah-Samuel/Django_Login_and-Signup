from . import views
from django.urls import path


urlpatterns = [
    # path('', views.landingpage, name='landingpage'),
    path('', views.register, name='register'),
    path('homepage/', views.homepage, name='homepage'),
    path('login/', views.logIn, name='login'),
]
