from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^new/', views.create_post, name="create_post"),
    url(r'^read/(?P<id>\d+)/$', views.read_post, name="read_post"),
    url(r'^update/(?P<id>\d+)/$', views.update_post, name="update_post"),
    url(r'^delete/(?P<id>\d+)/$', views.delete_post, name="delete_post"),
]
