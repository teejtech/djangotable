from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Musician
#

def home(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def hotel(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
def data(request):
    m=Musician.objects.all().values()
    template=loader.get_template('musician.html')
    context={
        'msanii':m,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('mform.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    a=request.POST['first']
    b=request.POST['last']
    c=request.POST['instrument']
    d=request.POST['age']
    e=request.POST['job']
    m=Musician(first_name=a,last_name=b,instrument=c, age=d,emp=e)
    m.save()
    return HttpResponseRedirect(reverse('data'))
def delete(request, id):
    m=Musician.objects.get(id=id)
    m.delete()
    return HttpResponseRedirect(reverse('data'))
def update(request, id):
    m=Musician.objects.get(id=id)
    template = loader.get_template('update.html')
    context ={
        'm':m,
    }
    return HttpResponse(template.render(context, request))
def updaterecord(request, id):
    a=request.POST['first']
    b=request.POST['last']
    c=request.POST['instrument']
    d=request.POST['age']
    e=request.POST['job']
    m = Musician.objects.get(id=id)
    m.first_name=a
    m.last_name=b
    m.instrument=c
    m.age=d
    m.emp=e
    m.save()
    return HttpResponseRedirect(reverse('data'))