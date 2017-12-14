from django.conf.urls import url
from . import views

app_name = 'Movie'
urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^signup/$',views.registeration, name='registeration'),
    url(r'^logout/$',views.Logout, name='logout')
]