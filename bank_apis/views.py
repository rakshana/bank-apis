# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.views import View
from models import Branches


def index(request):
    return HttpResponse('yay me')


class BankIFSCView(View):
    def get(self, request, code):
        bank_detail_values = ('bank__name', 'district', 'city', 'state', 'address')
        bank_details = Branches.objects.filter(ifsc=code).values(*bank_detail_values)
        return HttpResponse(status=200, content=json.dumps(list(bank_details)))


class BankByCityView(View):

    def get(self, request, **kwargs):
        bank_name = (kwargs.get('name')).upper()
        city = (kwargs.get('city')).upper()
        all_banks = Branches.objects.filter(bank__name=bank_name, city=city).values()
        return HttpResponse(status=200, content=json.dumps(list(all_banks)))

