from django.shortcuts import redirect
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin_page/add_app/', views.redirect_add_app),
    path('add_app/', views.add_app, name = 'add_app'),  

]

