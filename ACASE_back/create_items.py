#!/usr/bin/python3
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acase_v1.settings")
django.setup()

from storage.models import Item

with open("test.json", "r") as data:
    data = json.load(data)

    for element in data:
        for key, value in element.items():
            if key == 'url':
                if Item.objects.filter(url=value).count() >= 1:
                    pass
                else:
                    Item.objects.create(**element)
