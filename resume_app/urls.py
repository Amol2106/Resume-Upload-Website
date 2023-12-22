from django.urls import path
from resume_app import views

urlpatterns = [
    path('upload/', views.upload_resume, name='upload_resume'),
    path('profile/', views.view_profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.register, name='register'),
]