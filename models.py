# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Shopeeuser(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

class Products(models.Model):
	id = models.CharField(max_length=10,primary_key=True)
	name = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	price = models.IntegerField()
	