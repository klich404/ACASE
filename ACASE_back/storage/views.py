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
        json.dumps([{'Word':attr.Word} for attr in list(obj)]))


def target(request):
    obj = list(Target.objects.all())
    return HttpResponse(
        json.dumps([{'Name':attr.Name,
                     'Base_url':attr.Base_url} for attr in list(obj)]))

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
        print(request.POST.get('id'))
        print("-----------")
        print(request.POST.get('My_selection'))
        data = {}
        data['id'] = request.POST['id']
        data['My_selection'] = request.POST['My_selection']
        print(data)
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
        data['id'] = request.POST['id']
        data['Trash_selection'] = request.POST['Trash_selection']
        for key, value in data.items():
            if key == 'id':
                id_num = value
        Item.objects.filter(id=id_num).update(**data)
        return HttpResponse('melo caramelo')
    return HttpResponse('todo mal')
