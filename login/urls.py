from django.conf.urls import patterns, include, url


urlpatterns = patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login/login.html'}, name='login'),
    url(r'^logout/$', 'logout', {'template_name': 'login/logout.html'}, name='logout'),
)