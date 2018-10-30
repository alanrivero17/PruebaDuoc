from django.conf.urls import include, url
from . import views
from blog import views


urlpatterns = [
    url(r'^$', views.base_list),
    ]
