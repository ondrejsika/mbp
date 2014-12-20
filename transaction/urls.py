from django.conf.urls import patterns, include, url

urlpatterns = patterns('transaction.views',
    url(r'^payment-create/$', 'create_view', name='payment_create'),
    url(r'^payment-detail/(?P<token>[0-9a-zA-Z-]+)/$', 'payment_view', name='payment_detail'),
    url(r'^creator/(?P<profile_id>\d+)/$', 'creator_view', name='creator'),
)