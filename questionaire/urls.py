from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'questionaire'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<questionaire_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout, {'next_page': '/questionaire'}),
]
