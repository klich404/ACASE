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
    url                  = models.SlugField(max_length=200, blank=False) #SlogField is a validation for urls
    date                 = models.DateTimeField()
    text                 = models.TextField(blank=True)
    languaje             = models.CharField(max_length=6, choices=available_languajes, default='OTHER', blank=False) #choices choice between the objects of the list
    vigilance_category   = models.TextField(blank=True)
    information_category = models.TextField(blank=True)
    cita                 = models.CharField(max_length=200, blank=True)
