# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import json
from django.http import HttpResponse
from django.views import View
from models import Branches
import exceptions


def index(request):
    return HttpResponse('yay me')


class BankIFSCView(View):

    def get(self, request, code):
        bank_detail_values = ('bank__name', 'district', 'city', 'state', 'address')
        try:
            bank_details = Branches.objects.filter(ifsc=code).values(*bank_detail_values)
            return HttpResponse(status=200, content=json.dumps(list(bank_details)))
        except exceptions.IndexError:
            return HttpResponse(status=400)


class BankByCityView(View):

    def get(self, request, **kwargs):
        bank_name = (kwargs.get('name')).upper()
        city = (kwargs.get('city')).upper()
        try:
            all_banks = Branches.objects.filter(bank__name=bank_name, city=city).values()
            return HttpResponse(status=200, content=json.dumps(list(all_banks)))
        except IndexError:
            return HttpResponse(status=400)

