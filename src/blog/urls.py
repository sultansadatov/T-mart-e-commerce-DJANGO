from django import views
from django.urls import path
from . import views


urlpatterns = [

    path("blogs/<int:blog_id>", views.blog),
    path("bloglist", views.bloglist)
 
]
 