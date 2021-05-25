from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_posts, name="blog"),
    path("post/<url>/", views.blog_post, name="blog_post"),
    path("add/", views.add_post, name="add_post"),
    path("edit_post/<url>/", views.edit_post, name="edit_post"),
    path("delete_post/<url>/", views.delete_post, name="delete_post"),
]
