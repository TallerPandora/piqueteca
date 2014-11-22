from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'piqueteca.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'piqueteca_app.views.register', name='register'), # ADD NEW PATTERN!
    url(r'^piqueteca_app/register/$', 'piqueteca_app.views.register', name='registers'),
    url(r'^$', 'piqueteca_app.views.inicio', name='inicio')

)
