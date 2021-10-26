#!/usr/bin/python3
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acase_v1.settings")
django.setup()

from storage.models import Item

with open("update.json", "r") as data:
    data = json.load(data)

    for item in data:
        for key, value in item.items():
            if key == 'id':
                id_num = value
        obj = Item.objects.filter(id=id_num).update(**item)
