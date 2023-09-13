from django.db import models

from django.shortcuts import render

# Create your models here.

from item.models import Category, Item


def index(request):
    items= Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html',{
        "items": items,
        "categories": categories})

def index(request):

    render(request, 'core/contact.html')