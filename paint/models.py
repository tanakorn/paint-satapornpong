from django.db import models

class Brand(models.Model):
  name = models.CharField(max_length=32)

  def __unicode__(self):
    return self.name

class Product(models.Model):
  brand = models.ForeignKey(Brand)
  name = models.CharField(max_length=32)

  def __unicode__(self):
    return self.brand.name + ' ' + self.name

class Function(models.Model):
  name = models.CharField(max_length=32)

  def __unicode__(self):
    return self.name

class Size(models.Model):
  value = models.CharField(max_length=32)

  def __unicode__(self):
    return self.value

class Base(models.Model):
  name = models.CharField(max_length=16)

  def __unicode__(self):
    return self.name

class Paint(models.Model):
  product = models.ForeignKey(Product)
  function = models.ForeignKey(Function)
  size = models.ForeignKey(Size)
  base = models.ForeignKey(Base)

  def __unicode__(self):
    return self.product.brand.name + ' ' + self.product.name + ' ' + self.function.name + ' ' + self.size.value + ' ' + self.base.name

class Customer(models.Model):
  name = models.CharField(max_length=128)

  def __unicode__(self):
    return self.name

class Sell(models.Model):
  paint = models.ForeignKey(Paint)
  code = models.CharField(max_length=16)
  unit = models.IntegerField()
  price = models.FloatField()
  customer = models.ForeignKey(Customer, null=True)
  note = models.TextField()
  date = models.DateTimeField('Date')
