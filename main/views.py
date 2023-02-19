from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Items

def index(response):
    return HttpResponse("Hello World, here we go once again, that\'s my Django Project")

#def index(response, id):
 #   return HttpResponse("<h1>%s</h1>"% id)   #its a first way of a dynamic pages in terms of linking

def list(response, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.items_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, str(item.text)))

# Create your views here.
