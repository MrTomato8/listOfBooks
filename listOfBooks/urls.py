from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'books.views.main', name='main'),
    url(r'^books/(\d+)/$', 'books.views.detail', name='detail'),
    url(r'^admin/', include(admin.site.urls)),
)
