from django.conf.urls import patterns, include, url


urlpatterns = patterns('django.contrib.auth.views',
    url(r'^password-reset/$', 'password_reset',
        {'template_name': 'password_reset/password_reset.html'}, name='password_reset'),
    url(r'^password-reset/done/$', 'password_reset_done',
        {'template_name': 'password_reset/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>.*)/(?P<token>.*)/$', 'password_reset_confirm',
        {'template_name': 'password_reset/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^password-reset/complete/', 'password_reset_complete',
        {'template_name': 'password_reset/password_reset_complete.html'}, name='password_reset_complete'),
)