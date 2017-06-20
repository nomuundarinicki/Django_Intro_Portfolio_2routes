from django.conf.urls import url
from . import views
#from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index2', views.index2),
]


#index2 is my second route !
