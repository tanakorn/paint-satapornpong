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
  product = models.ForeignKey(Product)
  name = models.CharField(max_length=32)

  def __unicode__(self):
    return self.product.brand.name + ' ' + self.product.name + ' ' + self.name

class Size(models.Model):
  function = models.ForeignKey(Function)
  value = models.CharField(max_length=32)

  def __unicode__(self):
    return self.product.brand.name + ' ' + self.product.name + ' ' + self.value

class Base(models.Model):
  function = models.ForeignKey(Function)
  name = models.CharField(max_length=16)

  def __unicode__(self):
    return self.product.brand.name + ' ' + self.product.name + ' ' + self.name

class Customer(models.Model):
  name = models.CharField(max_length=128)

  def __unicode__(self):
    return self.name

class Sell(models.Model):
  function = models.ForeignKey(Function)
  size = models.ForeignKey(Size)
  base = models.ForeignKey(Base)
  code = models.CharField(max_length=8)
  unit = models.IntegerField()
  price = models.FloatField()
  customer = models.ForeignKey(Customer, null=True)
  note = models.TextField()
  date = models.DateTimeField('Date')
