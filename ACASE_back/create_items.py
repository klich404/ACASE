#!/usr/bin/python3
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acase_v1.settings")
django.setup()

from storage.models import Item, Keyword

with open("data.json", "r") as data:
    data = json.load(data)

    kws = []
    for element in data:
        for key, value in element.items():
            if key == 'Associated_KW':
                kws.append(value)
                kws = list(set(kws))
            if key == 'Url':
                if Item.objects.filter(Url=value).count() >= 1:
                    pass
                else:
                    Item.objects.create(**element)

for kw in kws:
    if Keyword.objects.filter(Word=kw).count() >= 1:
        pass
    else:
        Keyword.objects.create(Word=kw)
for word in kws:
    objs = Item.objects.filter(Associated_KW=word)
    kw = Keyword.objects.get(Word=word)
    kw.objs.add(*objs)
