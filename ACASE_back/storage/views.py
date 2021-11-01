from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from storage.models import Item, Keyword, Target
import json


def retrieve_items(request):
    obj = list(Item.objects.all())
    return HttpResponse(
        json.dumps([{'id':attr.id,
                     'Title':attr.Title,
                     'Url':attr.Url,
                     'Date':attr.Date,
                     'Source_url': attr.Source_url,
                     'Associated_KW': attr.Associated_KW,
                     'Text':attr.Text,
                     'My_selection': attr.My_selection,
                     'Trash_section': attr.Trash_section,
                     'Relevance':attr.Relevance,
                     'Learning':attr.Learning,
                     'Finding':attr.Finding,
                     'Pages':attr.Pages} for attr in list(obj)]))


def keywords(request):
    obj = list(Keyword.objects.all())
    return HttpResponse(
        json.dumps([{'Word':attr.Word,
                     'Items':attr.Items} for attr in list(obj)]))


def target(request):
    obj = list(Target.objects.all())
    return HttpResponse(
        json.dumps([{'Base_url':attr.Base_url,
                     'Items':attr.Items} for attr in list(obj)]))

@csrf_exempt
def update(request):
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
        return HttpResponse('melo caramelo')
    return HttpResponse('todo mal')


@csrf_exempt
def to_my_selection(request):
    if request.method == 'POST':
        data = {}
        for data in request.POST.keys():
            data = json.loads(data)
        for key, value in data.items():
            if key == 'id':
                id_num = value
        Item.objects.filter(id=id_num).update(**data)
        return HttpResponse('melo caramelo')
    return HttpResponse('todo mal')


@csrf_exempt
def to_trash_section(request):
    if request.method == 'POST':
        data = {}
        for data in request.POST.keys():
            data = json.loads(data)
        for key, value in data.items():
            if key == 'id':
                id_num = value
        Item.objects.filter(id=id_num).update(**data)
        return HttpResponse('melo caramelo')
    return HttpResponse('todo mal')
