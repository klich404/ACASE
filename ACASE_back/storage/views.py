from django.shortcuts import render
from django.http import HttpResponse
from storage.models import Item, Keyword, Target
import pdb
import json


def retrieve_items(request):
    obj = list(Item.objects.all())
    return HttpResponse(
        json.dumps([{'title':attr.title,
                     'url':attr.url,
                     'date':attr.date.strftime('%Y-%m-%d'),
                     'text':attr.text} for attr in list(obj)]))


def keywords(request):
    obj = list(Keyword.objects.all())
    return HttpResponse(
        json.dumps([{'word':attr.word} for attr in list(obj)]))


def target(request):
    obj = list(Target.objects.all())
    return HttpResponse(
        json.dumps([{'name':attr.name,
                     'base_url':attr.base_url} for attr in list(obj)]))
