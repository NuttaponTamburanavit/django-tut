# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Hello Python variable'
    context = {
      'title': title
    }
    return render(request, 'index.html', context)
