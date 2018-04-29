
from django.conf.urls import url,include
from django.contrib import admin
import group.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', include('signup.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^home/',group.views.homepage),
    url(r'^contactus/',group.views.contact),
    url(r'^about/', group.views.about),
    url(r'^welcome/', group.views.signlog),
    url(r'^teacherlogin/', include('teacherlog.urls')),
]
urlpatterns += staticfiles_urlpatterns()
