from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^travels$', views.dashboard, name="dashboard"),
    url(r'^travels/destination/(?P<id>\d+)/$', views.destination, name="destination"),
    url(r'^travels/add$', views.add_page, name='add_page'),
    url(r'^travels/add/trip', views.add, name="add"),
    url(r'^travels/join/(?P<id>\d+)/$', views.join, name='join'),
]
