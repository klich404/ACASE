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
            print(key, value)

    objs = Item.objects.all()
    objs = json.dumps([{'id':attr.id,
                        'title':attr.title,
                        'url':attr.url,
                        'date':attr.date,
                        'source_url': attr.source_url,
                        'Associated_KW': attr.Associated_KW,
                        'text':attr.text,
                        'relevance':attr.relevance,
                        'learning':attr.learning,
                        'finding':attr.finding,
                        'page':attr.pages} for attr in list(objs)])
    print(objs)
    