#!/usr/bin/python3
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acase_v1.settings")
django.setup()

from storage.models import Item

with open("data.json", "r") as data:
    data = json.load(data)

    for element in data:
        Item.objects.create(**element)
