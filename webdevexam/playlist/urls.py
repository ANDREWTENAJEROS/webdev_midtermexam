from django.conf.urls import url
from . import views
from playlist import views

app_name= 'playlist' #from create app


urlpatterns = [
    # /
    url(r'^$', views.IndexView, name='index'),
]
