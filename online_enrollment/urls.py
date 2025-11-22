from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),

    path('profile/', views.user_profile, name='user_profile'),
    path('enroll/', views.enrollment_form, name='enrollment_form'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
