from django.conf.urls import patterns, include, url

urlpatterns = patterns('profile.views',
    url(r'^(?P<profile_id>\d+)/$', 'detail_view', name='detail'),
    url(r'^(?P<profile_id>\d+)/edit/$', 'edit_view', name='edit'),
    url(r'^new/$', 'edit_view', name='new'),
)
