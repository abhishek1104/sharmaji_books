from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^search/$', views.search , name='search'),
    url(r'^contact/$', views.contact, name ='contact'),
    url(r'^thanks/$', views.thanksji, name ='thanksbaboo' ),
    url(r'^publishers/$',views.PublisherList.as_view() , name='publishers'),
    url(r'^overallbooks/$', views.PublisherList1.as_view(), name ='publishers1'),
    url(r'^books/([\w-]+)/$', views.PublisherList2.as_view(), name ='publishers2'),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetailView.as_view(), name='authordetail'),
]