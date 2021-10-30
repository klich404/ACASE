#!/usr/bin/python3
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acase_v1.settings")
django.setup()

from storage.models import Item, Keyword

with open("data.json", "r") as data:
    data = json.load(data)

    for element in data:
        for key, value in element.items():
            if key == 'Url':
                if Item.objects.filter(Url=value).count() >= 1:
                    pass
                else:
                    Item.objects.create(**element)

agil_objs = Item.objects.all(Associated_KW='agil')
agil_kw = Keyword.objects.get(Word='agil')
agil_kw.agil_objs.add(*agil_objs)

liderazgo_objs = Item.objects.all(Associated_KW='liderazgo')
liderazgo_kw = Keyword.objects.get(Word='liderazgo')
liderazgo_kw.liderazgo_objs.add(*liderazgo_objs)

seguridad_obj = Item.objects.all(Associated_KW='seguridad')
seguridad_kw = Keyword.objects.get(Word='seguridad')
seguridad_kw.seguridad_objs.add(*seguridad_objs)
