# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from triptricks.models import UserProfile
admin.site.register(UserProfile)
