from django.conf.urls import patterns, include, url

urlpatterns = patterns('profile.views',
    url(r'^(?P<profile_id>\d+)/$', 'detail_view', name='detail'),
)
