# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserProfile(models.Model):
	name = models.CharField(max_length=50)
	#username = models.CharField(max_length=50)
	#password = models.CharField(max_length=20)
	def __str__(self):
		return self.name


