from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$', 'books.views.main', name='main'),
    url(r'^books/(\d+)/$', 'books.views.detail', name='detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
