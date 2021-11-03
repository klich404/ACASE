from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from storage.models import Item, Keyword, Target
from django.shortcuts import redirect
import json


def retrieve_items(request):
    """Return a Item object"""
    obj = list(Item.objects.all())
    return HttpResponse(
        json.dumps([{'id': attr.id,
                     'Title': attr.Title,
                     'Url': attr.Url,
                     'Date': attr.Date,
                     'Source_url': attr.Source_url,
                     'Associated_KW': attr.Associated_KW,
                     'Text': attr.Text,
                     'My_selection': attr.My_selection,
                     'Trash_section': attr.Trash_section,
                     'Relevance': attr.Relevance,
                     'Learning': attr.Learning,
                     'Finding': attr.Finding,
                     'Pages': attr.Pages} for attr in list(obj)]))


def keywords(request):
    """Return a Keyword object"""
    obj = list(Keyword.objects.all())
    keywords = []
    for attr in obj:
        keywords.append(attr.Word)
    return HttpResponse(json.dumps(keywords))


def target(request):
    """Return a Target object"""
    obj = list(Target.objects.all())
    urls = []
    for attr in obj:
        urls.append(attr.Base_url)
    return HttpResponse(json.dumps(urls))


@csrf_exempt
def update(request):
    """Receives data from a form to update an Item object"""
    if request.method == 'POST':
        data = {}
        data['id'] = request.POST['id']
        data['Relevance'] = request.POST['Relevance']
        data['Learning'] = request.POST['Learning']
        data['Finding'] = request.POST['Finding']
        data['Pages'] = request.POST['Pages']
        for key, value in data.items():
            if key == 'id':
                id_num = value
        Item.objects.filter(id=id_num).update(**data)
        return HttpResponseRedirect('http://127.0.0.1:5500/Frontend/index.html')
    return HttpResponseRedirect('http://127.0.0.1:5500/Frontend/index.html')


@csrf_exempt
def to_my_selection(request):
    """Receive data to update a Item object"""
    if request.method == 'POST':
        data = {}
        for data in request.POST.keys():
            data = json.loads(data)
        for key, value in data.items():
            if key == 'id':
                id_num = value
        Item.objects.filter(id=id_num).update(**data)
        return HttpResponseRedirect('http://127.0.0.1:5500/Frontend/index.html')
    return HttpResponseRedirect('http://127.0.0.1:5500/Frontend/index.html')


@csrf_exempt
def to_trash_section(request):
    """Receive data to update a Item object"""
    if request.method == 'POST':
        data = {}
        for data in request.POST.keys():
            data = json.loads(data)
        for key, value in data.items():
            if key == 'id':
                id_num = value
        Item.objects.filter(id=id_num).update(**data)
        return HttpResponseRedirect('http://127.0.0.1:5500/Frontend/index.html')
    return HttpResponseRedirect('http://127.0.0.1:5500/Frontend/index.html')


@csrf_exempt
def run_bot(request):
    """Receive data to run scraper-bot"""
    if request.method == 'POST':
        data = json.loads(request.body)
        if data:
            kws = []
            source_url = []
            for element in data:
                for key, value in element.items():
                    if key == 'Source_url':
                        source_url.append(value)
                        source_url = list(set(source_url))  # save all the source url
                    if key == 'Associated_KW':
                        kws.append(value)
                        kws = list(set(kws))  # save all the keywords
                    if key == 'Url':
                        if Item.objects.filter(Url=value).count() >= 1:  # don't repeat items
                            pass
                        else:
                            Item.objects.create(**element)  # create the new items
                            for kw in kws:
                                # don't repeat keywords
                                if Keyword.objects.filter(Word=kw).count() >= 1:
                                    pass
                                else:
                                    # create the new keyword
                                    Keyword.objects.create(Word=kw)
                            for word in kws:
                                objs = Item.objects.filter(Associated_KW=word)
                                kw = Keyword.objects.get(Word=word)
                                kw.Items.add(*objs)  # create new m2m relationship
                            for sour_url in source_url:
                                # don't repeat urls
                                if Target.objects.filter(Base_url=sour_url).count() >= 1:
                                    pass
                                else:
                                    # create the new url
                                    Target.objects.create(Base_url=sour_url)
                            for s_url in source_url:
                                objs = Item.objects.filter(Associated_KW=s_url)
                                url = Target.objects.get(Base_url=s_url)
                                url.Items.add(*objs)  # create new m2m relationship
            return HttpResponse('Data succesfully obtained')
        return HttpResponse('Data missed')
    return HttpResponse('Bad request')
