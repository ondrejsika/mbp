from django.conf.urls import patterns, include, url

urlpatterns = patterns('account.views',
    url(r'^$', 'dashboard_view', name='dashboard'),
)
