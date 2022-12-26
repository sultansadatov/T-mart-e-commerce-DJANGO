from django import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from users import views as user_views



app_name = "user"

urlpatterns = [

  
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("logout/", user_views.logout_user, name = "logout"),


    path("wishlist", views.wishlist),
    path('register/', user_views.register, name='register'),
    path('password_reset/', user_views.password_reset, name='password_reset'),

    path(
        'change_password/',
        auth_views.PasswordChangeView.as_view(
            template_name='password/change_password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
 
]
