from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path("", views.MainPage.as_view(), name="main_page"),
    path("<int:pk>/insurance_details/", views.InsuranceDetail.as_view(), name= "insurance_details"),
    path('register/', views.register, name = 'register' ),
    path('login/', views.UserViewLogin.as_view(), name = "login"),
    path('logout/', views.logout_user, name = 'logout'),
    path('profile/', views.profile, name= "profile" ),
    path('user_update/', views.user_update, name= 'user_update'),
    path('user_products/', views.products_user, name='user_products'),
    ]   