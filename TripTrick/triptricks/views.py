# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    #template = loader.get_template('triptricks/index.html')
    #return HttpResponse("Hello, world. You're at the tritricks index.")
    return render(request, 'triptricks/index.html')
    #return render(request, template)
def signin(request):
    return render(request, 'triptricks/signin.html')
   



	