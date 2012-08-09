from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings

from paint.models import Brand, Product, Function, Size, Base, Sell

import os.path
import datetime

def index(request):
  return render_to_response('index.html', {})

def addSellRecord(request):
  return HttpResponseRedirect(reverse('paint.views.chooseBrand'))

def chooseBrand(request):
  allBrand = Brand.objects.all()
  return render_to_response('choose_brand.html', {'brand_list': allBrand}, context_instance=RequestContext(request))

def chooseProduct(request, brand_id):
  brand = get_object_or_404(Brand, id=brand_id)
  allProduct = brand.product_set.all()
  return render_to_response('choose_product.html', {'brand_name': brand.name, 'product_list': allProduct, 'brand': brand }, context_instance=RequestContext(request))

def chooseFunction(request, product_id):
  product = get_object_or_404(Product, id=product_id)
  allFunction = product.function_set.all()
  return render_to_response('choose_function.html', {'brand_name': product.brand.name, 'product_name': product.name, 'function_list': allFunction}, context_instance=RequestContext(request))

def enterDetail(request, function_id):
  function = get_object_or_404(Function, id=function_id)
  allSize = function.sizes.all()
  allBase = function.bases.all()
  return render_to_response('enter_detail.html', {'brand_name': function.product.brand.name, 'product_name': function.product.name, 'function_name': function.name, 'function_id': function_id, 'size_list': allSize, 'base_list': allBase}, context_instance=RequestContext(request))

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

def search(request):
  return HttpResponseRedirect(reverse('paint.views.selectSearch'))

def selectSearch(request):
  return render_to_response('search_select.html', {})

def searchByDate(request, day=0, month=0, year=0):
  if day == 0 or month == 0 or year == 0:
    searchDate = datetime.date.today()
  else:
    searchDate = datetime.date(int(year), int(month), int(day))
  sellRecords = Sell.objects.filter(date=searchDate)
  oneday = datetime.timedelta(1)
  previousDay = searchDate - oneday
  nextDay = searchDate + oneday
  return render_to_response('search_date.html', {'sell_record_list': sellRecords, 'date': searchDate, 'previous_day': previousDay, 'next_day': nextDay}, context_instance=RequestContext(request))

def searchByMonth(request, month=0, year=0):
  if month == 0 or year == 0:
    searchDate = datetime.date.today()
  else:
    searchDate = datetime.date(int(year), int(month), 1)
  sellRecords = Sell.objects.filter(date__month=searchDate.month, date__year=searchDate.year)
  sorted(sellRecords, key=lambda record: record.date)
  previousMonth = {}
  previousMonth['month'] = searchDate.month - 1 if searchDate.month != 1 else 12
  previousMonth['year'] = searchDate.year if searchDate.month != 1 else searchDate.year - 1
  nextMonth = {}
  nextMonth['month'] = searchDate.month + 1 if searchDate.month != 12 else 1
  nextMonth['year'] = searchDate.year if searchDate.month != 12 else searchDate.year + 1
  return render_to_response('search_month.html', {'sell_record_list': sellRecords, 'date': searchDate, 'previous_month': previousMonth, 'next_month': nextMonth}, context_instance=RequestContext(request))

def enterCustomer(request):
  return render_to_response('enter_customer.html', {})

def searchByCustomer(request, customer, month=0, year=0):
  if month == 0 or year == 0:
    searchDate = datetime.date.today()
  else:
    searchDate = datetime.date(int(year), int(month), 1)
  sellRecords = Sell.objects.filter(customer__startswith=customer, date__month=searchDate.month, date__year=searchDate.year)
  sorted(sellRecords, key=lambda record: record.date)
  previousMonth = {}
  previousMonth['month'] = searchDate.month - 1 if searchDate.month != 1 else 12
  previousMonth['year'] = searchDate.year if searchDate.month != 1 else searchDate.year - 1
  nextMonth = {}
  nextMonth['month'] = searchDate.month + 1 if searchDate.month != 12 else 1
  nextMonth['year'] = searchDate.year if searchDate.month != 12 else searchDate.year + 1
  return render_to_response('search_customer.html', {'customer': customer, 'sell_record_list': sellRecords, 'date': searchDate, 'previous_month': previousMonth, 'next_month': nextMonth}, context_instance=RequestContext(request))

def enterCode(request):
  return render_to_response('enter_code.html', {})

def searchByCode(request, code, month=0, year=0):
  if month == 0 or year == 0:
    searchDate = datetime.date.today()
  else:
    searchDate = datetime.date(int(year), int(month), 1)
  sellRecords = Sell.objects.filter(code__endswith=code, date__month=searchDate.month, date__year=searchDate.year)
  sorted(sellRecords, key=lambda record: record.date)
  previousMonth = {}
  previousMonth['month'] = searchDate.month - 1 if searchDate.month != 1 else 12
  previousMonth['year'] = searchDate.year if searchDate.month != 1 else searchDate.year - 1
  nextMonth = {}
  nextMonth['month'] = searchDate.month + 1 if searchDate.month != 12 else 1
  nextMonth['year'] = searchDate.year if searchDate.month != 12 else searchDate.year + 1
  return render_to_response('search_code.html', {'code': code, 'sell_record_list': sellRecords, 'date': searchDate, 'previous_month': previousMonth, 'next_month': nextMonth}, context_instance=RequestContext(request))
