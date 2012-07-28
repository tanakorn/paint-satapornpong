from django.db import models

class Brand(models.Model):
  name = models.CharField(max_length=32)

class Category(models.Model):
  brand = models.ForeignKey(Brand)
  name = models.CharField(max_length=32)

class SubCategory(models.Model):
  category = models.ForeignKey(Category)
  name = models.CharField(max_length=32)

class Size(models.Model):
  category = models.ForeignKey(Category)
  value = models.CharField(max_length=32)

class Base(models.Model):
  category = models.ForeignKey(Category)
  value = models.CharField(max_length=16)

class Customer(models.Model):
  name = models.CharField(max_length=128)

class Sell(models.Model):
  subCategory = models.ForeignKey(SubCategory)
  size = models.ForeignKey(Size)
  base = models.ForeignKey(Base)
  code = models.CharField(max_length=8)
  unit = models.IntegerField()
  price = models.FloatField()
  customer = models.ForeignKey(Customer, null=True)
  note = models.TextField()
