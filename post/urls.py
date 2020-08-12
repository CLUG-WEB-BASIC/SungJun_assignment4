from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.read_blog_list,name = "read_blog_list"),
    path('list/<int:blog_id>',views.read_blog_detail,name="read_blog_detail"),
    path('new/',views.blog_new,name = "blog_new"),
    path('create/',views.create_blog,name = "create_blog"),
]