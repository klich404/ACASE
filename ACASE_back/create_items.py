#!/usr/bin/python3
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acase_v1.settings")
django.setup()

from storage.models import Item, Keyword, Target

with open("data.json", "r") as data:
    data = json.load(data) #save the info

    kws = []
    source_url = []
    for element in data:
        for key, value in element.items():
            if key == 'Source_url':
                source_url.append(value)
                source_url = list(set(source_url)) #save all the source url
            if key == 'Associated_KW':
                kws.append(value)
                kws = list(set(kws)) #save all the keywords
            if key == 'Url':
                if Item.objects.filter(Url=value).count() >= 1: #don't repeat items
                    #print("This Item already exists")
                    pass
                else:
                    Item.objects.create(**element) #create the new items
                    #print("New Item created!")
                    for kw in kws:
                        if Keyword.objects.filter(Word=kw).count() >= 1: #don't repeat keywords
                            #print("This Keyword already exists")
                            pass
                        else:
                            Keyword.objects.create(Word=kw) #create the new keyword
                            #print("New Keyword created!")
                    for word in kws:
                        objs = Item.objects.filter(Associated_KW=word)
                        kw = Keyword.objects.get(Word=word)
                        kw.Items.add(*objs) #create new m2m relationship
                        #print("New relation Keyword-Item created!")
                    for sour_url in source_url:
                        if Target.objects.filter(Base_url=sour_url).count() >= 1: #don't repeat urls
                            #print("This Target already exists")
                            pass
                        else:
                            Target.objects.create(Base_url=sour_url) #create the new url
                            #print("New Target created!")
                    for s_url in source_url:
                        objs = Item.objects.filter(Associated_KW=s_url)
                        url = Target.objects.get(Base_url=s_url)
                        url.Items.add(*objs) #create new m2m relationship
                        #print("New relation Target-Item created!!")
