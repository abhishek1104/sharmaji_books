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
from .views import hello,current_Datetimereq,hours_ahead
#from books import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^time/$',current_Datetimereq),
    url(r'^another_time_page/$',current_Datetimereq),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead), # ^ is called carret sign!
    #url(r'^search-form/$' , views.search_form),
    #url(r'^search/$', views.search),s
    #url(r'^contact/$', views.contact),
    url(r'^', include('books.urls',namespace="mysite")),

]
