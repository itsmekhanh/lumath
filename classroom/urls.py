from django.conf.urls import patterns, url

from classroom import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^period/(?P<period_id>\d+)$', views.period, name='period'),
    url(r'^assignments/(?P<period_id>\d+)$', views.assignments, name='assignments'),
    url(r'^announcements/(?P<period_id>\d+)$', views.announcements, name='announcements'),
    url(r'^tests/(?P<period_id>\d+)$', views.tests, name='tests'),
    url(r'^contact$', views.contact, name='contact'),
)