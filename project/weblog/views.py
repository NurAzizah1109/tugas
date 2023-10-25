from django.shortcuts import render
from django.Http import HttpResponse
from django.template import loader

def weblog(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
def coba2(request):
     template=loader.get_template('coba2.html')
    return HttpResponse(template.render())

