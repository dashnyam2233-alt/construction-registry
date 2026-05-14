from django.urls import path
from . import community_views

app_name = "community"

urlpatterns = [
    path("", community_views.community_home, name="home"),
    path("new/", community_views.post_create, name="post_create"),
]
