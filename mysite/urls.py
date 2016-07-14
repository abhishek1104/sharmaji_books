"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings #For importing settings!
#from books import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',views.hello,name="mysite_hello"),
    #url(r'^time/$',views.current_Datetimereq,name="mysite_time"),
    #url(r'^time/plus/(-?\d{1,2})/$', views.hours_ahead), 
    #^ is called carret sign.-?means minus is optional.Allows -ve no.s too
    url(r'^time/',include([
        url(r'^$' ,views.current_Datetimereq,name="mysite_time"),
        url(r'^plus/(-?\d{1,2})/$' ,views.hours_ahead,name="mysite_hours_ahead"),
        url(r'^plus10/$' ,views.hours_ahead,{'offset':10},name="mysite_plus3"), #Pass value for view taken{'offset':10}!
        url(r'^plus_default/$' ,views.hours_ahead,name="mysite_plus_default"), #Default offset under view taken
        ])), #Only time/ upto url would be shown in debug mode,not other urls the part of include within it !
    url(r'^another_time_page/$',views.current_Datetimereq,name="mysite_another_time"),
    #url(r'^search-form/$' , views.search_form),
    #url(r'^search/$', views.search),
    #url(r'^contact/$', views.contact),
    url(r'^', include('books.urls',namespace="myapp")),
]


if settings.DEBUG:
    urlpatterns += [url(r'^timestamp/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$' ,views.timevalue),]
