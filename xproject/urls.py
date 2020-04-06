from django.contrib import admin
from django.urls import path,include,re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^chat/', include('chat.urls')),
    re_path('^rbac/',include('rbac.urls'))
]
