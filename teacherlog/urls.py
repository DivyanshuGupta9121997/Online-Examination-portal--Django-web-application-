from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.login_user, name='login'),
    url(r'^teacherdetail/',views.teacherdetail),
    #url(r'^p2p/$',views.p2p,name='p2p'),
]