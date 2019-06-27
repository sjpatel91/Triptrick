# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    
class Plan(models.Model):
	
	destination_name = models.CharField(max_length=200)
	number_days = models.PositiveSmallIntegerField(default=1, blank=True)
	sub_destination = models.TextField()
	description = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	



