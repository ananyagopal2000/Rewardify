from django.shortcuts import redirect
from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),    

    path('main_page/<int:user_id>/',views.main_page, name='main_page'),
    path('view_in_detail/<int:app_id>/<int:user_id>',views.view_in_detail, name='view_in_detail'),

    path('profile/<int:user_id>/', views.profile, name='profile'),
   
    path('points/<int:user_id>/', views.points, name='points'),
    # path('points/<int:user_id>/main_page', views.main_page, name='main_page'),

    path('tasks_completed/<int:user_id>/', views.tasks_completed, name='tasks_completed'),
    # path('tasks_completed/<int:user_id>/main_page', views.main_page, name='main_page'),

    path('signup/signup/', views.redirect_signup),
    path('login/login/', views.redirect_login),
    path('main_page/view_in_detail/', views.redirect_view_in_detail),
    path('main_page/<int:user_id>/profile/', views.redirect_profile),
    path('main_page/<int:user_id>/points/', views.redirect_points),
    path('main_page/<int:user_id>/tasks_completed/', views.redirect_tasks_completed),
    path('main_page/<int:user_id>/logout/', views.redirect_logout),
    path('main_page/<int:user_id>/upload_screenshot/', views.upload_screenshot, name='uploaded_screenshot'),
]

    # path('points/<int:user_id>/main_page', views.main_page, name='main_page'),

    # path('main_page/',views.main_page, name='main_page'),
        # path('points/<int:user_id>/', views.points, name='points'),

    # path('main_page/profile/<int:user_id>/', views.profile, name='profile'),
    
    # path('main_page/<int:user_id>/profile/<int:user_id>', views.incorrect_profile_redirect),
    # path('main_page/<int:user_id>/points/<int:user_id>', views.incorrect_points_redirect),



