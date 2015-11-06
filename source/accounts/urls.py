from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
)
