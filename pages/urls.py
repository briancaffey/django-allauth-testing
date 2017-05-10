from django.conf.urls import url, include
from .views import HomeView, profile_view

urlpatterns = [

    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^profile/$', profile_view, name="profile_view"),

]
