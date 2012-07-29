from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.conf import settings

from painting.models import Brand, Category

import os.path

def chooseBrand(request):
  allBrand = Brand.objects.all()
  for brand in allBrand:
    if os.path.isfile('%s/brand/%s.jpg' % (settings.STATIC_ROOT, brand.name)):
      brand.hasImage = True
    else:
      brand.hasImage = False
  return render_to_response('choose_brand.html', {'brand_list': allBrand}, context_instance=RequestContext(request))

def chooseCategory(request, brand_id):
  brand = get_object_or_404(Brand, id=brand_id)
  allCategory = brand.category_set.all()
  for category in allCategory:
    if os.path.isfile('%s/category/%s/%s.jpg' % (settings.STATIC_ROOT, brand.name, category.name)):
      category.hasImage = True
    else:
      category.hasImage = False
  return render_to_response('choose_category.html', {'category_list': allCategory, 'brand': brand }, context_instance=RequestContext(request))
