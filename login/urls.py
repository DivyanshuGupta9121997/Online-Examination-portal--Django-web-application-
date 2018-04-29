from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_user, name='login'),
    url(r'^rules/$',views.rules,name='rules'),
    url(r'^p2p/$',views.p2p,name='p2p'),
   # url(r'^hover/$',views.hoverpage,name='hover'),


]
