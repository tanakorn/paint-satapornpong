from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from painting.models import Brand

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'painting.views.chooseBrand'),

  # Uncomment the admin/doc line below to enable admin documentation:
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
)
