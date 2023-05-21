from . import views
from django.urls import path



urlpatterns = [ 
    path('',views.logIn, name='logIn'),
    path('register', views.register, name='register')
]