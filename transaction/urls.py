from django.conf.urls import patterns, include, url

urlpatterns = patterns('transaction.views',
    url(r'^create/$', 'create_view', name='create'),
    url(r'^payment/(?P<token>[0-9a-zA-Z-]+)/$', 'payment_view', name='payment'),
    url(r'^creator/(?P<profile_id>\d+)/$', 'creator_view', name='creator'),
)