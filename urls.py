from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^', include('account.urls', namespace='account')),
    url(r'^tr/', include('transaction.urls', namespace='tr')),
    url(r'^profile/', include('profile.urls', namespace='profile')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('login.urls')),
    url(r'^', include('password_reset.urls')),

)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

