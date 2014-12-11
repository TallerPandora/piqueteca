from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'piqueteca.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'piqueteca_app.views.register', name='register'),
    url(r'^inicio/$', 'piqueteca_app.views.inicio', name='inicio'),
    url(r'^inicioexterno/$', 'piqueteca_app.views.inicioexterno', name='inicioexterno')
)
