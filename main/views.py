from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Items

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

#def index(response, id):
 #   return HttpResponse("<h1>%s</h1>"% id)   #its a first way of a dynamic pages in terms of linking

  
def home(response):
    return render(response, "main/home.html", {})

