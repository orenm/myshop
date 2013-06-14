from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from oscar.app import application

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       (r'', include(application.urls)),
    # Examples:
    # url(r'^$', 'myshop.views.home', name='home'),
    # url(r'^myshop/', include('myshop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
