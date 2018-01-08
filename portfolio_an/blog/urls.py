from django.conf.urls import patterns, url

from portfolio_an.blog import views

urlpatterns = patterns('',
   url(r"^$", views.main, name="blog"),
   url(r"^(?P<pk>\d+)/$", views.post, name="post"),
   url(r"^add_comment/(?P<pk>\d+)/$", views.add_comment, name="add_comment"),
   url(r"^delete_comment/(?P<pk>\d+)/$", views.delete_comment, name="delete_comment"),
   url(r"^delete_comment/(?P<pk>\d+)/(\d+)/$", views.delete_comment, name="delete_comment"),
   url(r'^month/(?P<year>\d+)/(?P<month>\d+)/$', views.month, name="month"),
)
