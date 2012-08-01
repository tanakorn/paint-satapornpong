from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from paint.models import Brand

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^sell/brand/$', 'paint.views.chooseBrand'),
  url(r'^sell/product/(?P<brand_id>\d+)/$', 'paint.views.chooseProduct'),
  url(r'^sell/function/(?P<product_id>\d+)/$', 'paint.views.chooseFunction'),
  url(r'^sell/detail/(?P<function_id>\d+)/$', 'paint.views.enterDetail'),

  # Uncomment the admin/doc line below to enable admin documentation:
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
)
