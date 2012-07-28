from django.db import models

class Brand(models.Model):
  name = models.CharField(max_length=32)

  def __unicode__(self):
    return self.name

class Category(models.Model):
  brand = models.ForeignKey(Brand)
  name = models.CharField(max_length=32)

  def __unicode__(self):
    return self.brand.name + ' ' + self.name

class SubCategory(models.Model):
  category = models.ForeignKey(Category)
  name = models.CharField(max_length=32)

  def __unicode__(self):
    return self.category.brand.name + ' ' + self.category.name + ' ' + self.name

class Size(models.Model):
  category = models.ForeignKey(Category)
  value = models.CharField(max_length=32)

  def __unicode__(self):
    return self.category.brand.name + ' ' + self.category.name + ' ' + self.value

class Base(models.Model):
  category = models.ForeignKey(Category)
  name = models.CharField(max_length=16)

  def __unicode__(self):
    return self.category.brand.name + ' ' + self.category.name + ' ' + self.name

class Customer(models.Model):
  name = models.CharField(max_length=128)

  def __unicode__(self):
    return self.name

class Sell(models.Model):
  subCategory = models.ForeignKey(SubCategory)
  size = models.ForeignKey(Size)
  base = models.ForeignKey(Base)
  code = models.CharField(max_length=8)
  unit = models.IntegerField()
  price = models.FloatField()
  customer = models.ForeignKey(Customer, null=True)
  note = models.TextField()
  date = models.DateTimeField('Date')
