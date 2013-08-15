from django.conf.urls import patterns, url

from classroom import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^period/(?P<period_id>\d+)$', views.period, name='period'),
)