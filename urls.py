from django.conf.urls import patterns, include, url

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
