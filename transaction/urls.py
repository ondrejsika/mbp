from django.conf.urls import patterns, include, url

urlpatterns = patterns('transaction.views',
    url(r'^create/$', 'create_view', name='detail'),
    url(r'^detail/(?P<token>[0-9a-zA-Z-]+)/$', 'detail_view', name='detail'),
)