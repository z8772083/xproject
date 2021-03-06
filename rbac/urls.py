from django.urls import path,include,re_path
from django.views.decorators.csrf import csrf_exempt

from rbac import views
app_name = 'rbac'
urlpatterns = [
    re_path(r'^user/list/$',views.UserInfo.as_view(),name='user_list'),
    # re_path(r'^user/del/(?P<uid>\d+)/$', views.user_del, name='user_del'),
    re_path(r'^user/del/$', views.user_del, name='user_del'),
    re_path(r'^user/edit/(?P<uid>\d+)/$', views.user_edit, name='user_edit'),
    re_path(r'^user/add/$', views.user_add, name='user_add'),
    re_path(r'^chat/$',csrf_exempt(views.Chat.as_view()),name='chat'),
    re_path(r'^user/batch_del/$',views.user_batch_del,name='user_batch_del'),
    re_path(r'^url/(?P<proj>(g|r|l))/index/$',views.proj_index,name='proj_index'),

]
