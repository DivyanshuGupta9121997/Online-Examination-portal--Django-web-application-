from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.userview, name='signup'),
    url(r'^veri_page/$',views.verify,name='verify'),
]
