from django.conf.urls import patterns, url

from classroom import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)