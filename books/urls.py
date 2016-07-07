from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^search/$', views.search , name='search'),
    url(r'^contact/$', views.contact, name ='contact'),
    url(r'^thanks/$', views.thanksji, name ='thanksbaboo' ),
]