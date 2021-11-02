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
