from django.db import models

# Create your models here.
class Item(models.Model):
    available_languajes = [
        ('ESP', 'ESP'),
        ('ENG', 'ENG'),
        ('OTHER', 'OTHER')
    ]

    Created_at           = models.DateTimeField(auto_now_add=True) #auto_now_add modified the date only when is created
    Updated_at           = models.DateTimeField(auto_now=True) #auto_now_add modified the date averytime who is saved
    Title                = models.CharField(max_length=100, blank=False)
    Url                  = models.SlugField(max_length=200, blank=False) #SlugField is a validation for urls
    Source_url           = models.SlugField(max_length=200, blank=False)
    Associated_KW        = models.CharField(max_length=30, blank=False)
    Date                 = models.CharField(max_length=15, blank=False)
    Text                 = models.TextField(blank=True)
    Languaje             = models.CharField(max_length=6, choices=available_languajes, default='OTHER', blank=True) #choices choice between the objects of the list
    My_selection         = models.BooleanField(default=False)
    Trash_section        = models.BooleanField(default=False)
    Relevance            = models.TextField(null=True, blank=True, default=None)
    Learning             = models.TextField(null=True, blank=True, default=None)
    Finding              = models.TextField(null=True, blank=True, default=None)
    Page                = models.TextField(null=True, blank=True, default=None)

class Keyword(models.Model):
    Word  = models.CharField(max_length=30, blank=False)
    Items = models.ManyToManyField(Item)


class Target(models.Model):
    Name     = models.CharField(max_length=30, blank=False)
    Base_url = models.SlugField(max_length=200, blank=False)
