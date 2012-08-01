from django.db import models

class Brand(models.Model):
  name = models.CharField(max_length=32)

  def __unicode__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=32)
  brand = models.ForeignKey(Brand)

  def __unicode__(self):
    return self.brand.name + ' ' + self.name

class Size(models.Model):
  value = models.CharField(max_length=32)

  def __unicode__(self):
    return self.value

class Base(models.Model):
  name = models.CharField(max_length=16)

  def __unicode__(self):
    return self.name

class Function(models.Model):
  name = models.CharField(max_length=32)
  product = models.ForeignKey(Product)
  sizes = models.ManyToManyField(Size)
  bases = models.ManyToManyField(Base)

  def __unicode__(self):
    return self.name

class Customer(models.Model):
  name = models.CharField(max_length=128)

  def __unicode__(self):
    return self.name

class Sell(models.Model):
  function = models.ForeignKey(Function)
  size = models.ForeignKey(Size)
  base = models.ForeignKey(Base)
  code = models.CharField(max_length=16)
  unit = models.IntegerField()
  price = models.FloatField()
  customer = models.ForeignKey(Customer, null=True)
  note = models.TextField()
  date = models.DateTimeField()
