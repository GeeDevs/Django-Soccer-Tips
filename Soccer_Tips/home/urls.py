from django.conf.urls import url
from django.http import request
from home import views


urlpatterns = [
    url('', views.index, name ='index')
]
