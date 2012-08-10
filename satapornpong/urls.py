from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from paint.models import Brand

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'paint.views.index'),

  url(r'^sell/$', 'paint.views.addSellRecord'),
  url(r'^sell/brand/$', 'paint.views.chooseBrand'),
  url(r'^sell/product/(?P<brand_id>\d+)/$', 'paint.views.chooseProduct'),
  url(r'^sell/function/(?P<product_id>\d+)/$', 'paint.views.chooseFunction'),
  url(r'^sell/detail/(?P<function_id>\d+)/$', 'paint.views.enterDetail'),
  url(r'^sell/record/$', 'paint.views.record'),

  url(r'^search/$', 'paint.views.search'),
  url(r'^search/select/$', 'paint.views.selectSearch'),
  url(r'^search/date/$', 'paint.views.searchByDate'),
  url(r'^search/date/(?P<day>\d+)/(?P<month>\d+)/(?P<year>\d+)/$', 'paint.views.searchByDate'),
  url(r'^search/month/$', 'paint.views.searchByMonth'),
  url(r'^search/month/(?P<month>\d+)/(?P<year>\d+)/$', 'paint.views.searchByMonth'),
  url(r'^search/select/customer/$', 'paint.views.enterCustomer'),
  url(r'^search/customer/(?P<customer>\w+)/$', 'paint.views.searchByCustomer'),
  url(r'^search/customer/(?P<customer>\w+)/(?P<month>\d+)/(?P<year>\d+)/$', 'paint.views.searchByCustomer'),
  url(r'^search/select/code/$', 'paint.views.enterCode'),
  url(r'^search/code/(?P<code>\w+)/$', 'paint.views.searchByCode'),
  url(r'^search/code/(?P<code>\w+)/(?P<month>\d+)/(?P<year>\d+)/$', 'paint.views.searchByCode'),

  # Uncomment the admin/doc line below to enable admin documentation:
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
)
