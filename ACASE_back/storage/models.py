from django.db import models

# Create your models here.
class Item(models.Model):
    available_languajes = [
        ('ESP', 'ESP'),
        ('ENG', 'ENG'),
        ('OTHER', 'OTHER')
    ]

    created_at           = models.DateTimeField(auto_now_add=True) #auto_now_add modified the date only when is created
    updated_at           = models.DateTimeField(auto_now=True) #auto_now_add modified the date averytime who is saved
    title                = models.CharField(max_length=100, blank=False)
    url                  = models.SlugField(max_length=200, blank=False) #SlugField is a validation for urls
    source_url           = models.SlugField(max_length=200, blank=False)
    Associated_KW        = models.CharField(max_length=30, blank=False)
    date                 = models.CharField(max_length=15, blank=False)
    text                 = models.TextField(blank=True)
    languaje             = models.CharField(max_length=6, choices=available_languajes, default='OTHER', blank=False) #choices choice between the objects of the list
    relevance            = models.TextField(blank=True, default=None)
    learning             = models.TextField(blank=True, default=None)
    finding              = models.TextField(blank=True, default=None)
    pages                = models.TextField(blank=True, default=None)

class Keyword(models.Model):
    word  = models.CharField(max_length=30, blank=False)
    items = models.ManyToManyField(Item)


class Target(models.Model):
    name     = models.CharField(max_length=30, blank=False)
    base_url = models.SlugField(max_length=200, blank=False)
