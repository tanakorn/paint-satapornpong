from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings

from paint.models import Brand, Product, Function, Size, Base, Sell

import os.path
import datetime

def chooseBrand(request):
  allBrand = Brand.objects.all()
  for brand in allBrand:
    if os.path.isfile('%s/brand/%s.jpg' % (settings.STATIC_ROOT, brand.name)):
      brand.hasImage = True
    else:
      brand.hasImage = False
  return render_to_response('choose_brand.html', {'brand_list': allBrand}, context_instance=RequestContext(request))

def chooseProduct(request, brand_id):
  brand = get_object_or_404(Brand, id=brand_id)
  allProduct = brand.product_set.all()
  for product in allProduct:
    if os.path.isfile('%s/product/%s/%s.jpg' % (settings.STATIC_ROOT, brand.name, product.name)):
      product.hasImage = True
    else:
      product.hasImage = False
  return render_to_response('choose_product.html', {'product_list': allProduct, 'brand': brand }, context_instance=RequestContext(request))

def chooseFunction(request, product_id):
  product = get_object_or_404(Product, id=product_id)
  allFunction = product.function_set.all()
  return render_to_response('choose_function.html', {'function_list': allFunction}, context_instance=RequestContext(request))

def enterDetail(request, function_id):
  function = get_object_or_404(Function, id=function_id)
  allSize = function.sizes.all()
  allBase = function.bases.all()
  return render_to_response('enter_detail.html', { 'function_id': function_id, 'size_list': allSize, 'base_list': allBase}, context_instance=RequestContext(request))

def record(request):
  function_id = request.POST['function_id']
  size_id = request.POST['size_id']
  base_id = request.POST['base_id']
  code = request.POST['code']
  unit = request.POST['unit']
  price = request.POST['price']
  customer = request.POST['customer'] if request.POST['customer'] else None
  note = request.POST['note'] if request.POST['note'] else None
  function = Function.objects.get(id=function_id)
  size = Size.objects.get(id=size_id)
  base = Base.objects.get(id=base_id)
  sell = Sell(function=function, size=size, base=base, code=code, unit=unit, price=price, customer=customer, note=note)
  sell.save()
  return HttpResponseRedirect(reverse('paint.views.chooseBrand'))
