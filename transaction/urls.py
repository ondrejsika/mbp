from django.conf.urls import patterns, include, url

urlpatterns = patterns('transaction.views',
    url(r'^create/$', 'create_view', name='detail'),
    url(r'^payment/(?P<token>[0-9a-zA-Z-]+)/$', 'payment_view', name='payment'),
)