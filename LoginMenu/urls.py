from . import views
from django.urls import path



urlpatterns = [
    path('',views.landingpage,name='landingpage'),
    path('login/',views.logIn, name='logIn'),
    path('register/', views.register, name='register'),
    path('homepage/',views.homepage,name='homepage')
]