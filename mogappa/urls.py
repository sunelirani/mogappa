from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import logout, login

urlpatterns = [
    url(r'^$','login.views.post_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'login.views.login_user'),
    url(r'^home/', 'login.views.home'),
    url(r'^logout/', 'login.views.logout_user'),
    url(r'^signup/', 'login.views.signup_user'),
    url(r'^post/(?P<pk>[0-9]+)/$', 'login.views.post_detail'),
    url(r'^post/new/$', 'login.views.post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', 'login.views.post_edit'),
]    

