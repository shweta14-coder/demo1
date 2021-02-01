from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#create your views here.


def index(request):
    return HttpResponse("students list (index method). ")


def add(request):
    template = loader.get_template('add.html')

    result =[]

    print(request.GET)
    x = int(request.GET['num1' ])
    y = int(request.GET['num2' ])

    z = x + y

    result =[x,y,z]
    #print(z)

    #return HttpResponse("Addition: " + str(z))
    return HttpResponse(template.render())

  