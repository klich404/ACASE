from django.shortcuts import render
from django.http import HttpResponse
import json


def test(request):
    obj = []
    return HttpResponse(json.dumps(obj))


def keywords(request):
    obj = []
    return HttpResponse(json.dumps(obj))


def url(request):
    obj = []
    return HttpResponse(json.dumps(obj))
