from django.conf.urls import url,re_path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    re_path(r'^url/(?P<proj>(g|r|l))/index/$',views.chat_index,name='chat_index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]