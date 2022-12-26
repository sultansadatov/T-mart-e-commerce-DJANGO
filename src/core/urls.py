from django import views
from django.urls import path
from . import views


app_name = 'index'

urlpatterns = [

    path("", views.Index.as_view(template_name = 'core/index.html'), name="index"),
    path("about", views.about),
    path("team", views.team),
    path("contact", views.contact, name="contact"),
    path("password_reset/", views.password_reset_request, name="password_reset"),

]
