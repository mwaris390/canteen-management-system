from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import MyAppMembers

def index(request):
    q = MyAppMembers.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        'mymembers':q,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({},request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    q = MyAppMembers(firstname=x,lastname=y)
    q.save()
    return HttpResponseRedirect(reverse("index"))

def delrecord(request,id):
    q = MyAppMembers.objects.get(id=id)
    q.delete()
    return HttpResponseRedirect(reverse("index"))

def uprecord(request,id):
    q = MyAppMembers.objects.get(id=id)
    template = loader.get_template("update.html")
    context = {
        'mymembers':q,
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    f = request.POST["first"]
    l = request.POST["last"]
    q = MyAppMembers.objects.get(id=id)
    q.firstname = f
    q.lastname = l
    q.save()
    return HttpResponseRedirect(reverse("index"))
