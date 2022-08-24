from pickle import TRUE
from django.shortcuts import render
from http.client import HTTPResponse
from datetime import date, datetime
from AppCoderMarianoVanetta.models import Padres, Hijo

def main(request):
    mensaje="Bienvenido! las urls posible son /crear_familia y /ver_familia"
    return HTTPResponse(mensaje)


def crear_familia(request):

    #  today =date.today() 
    # edad = today.year-fecha_nac
    # if edad < 18:
    #     familia1 = Hijo(nombre,apellido,edad,fecha_nac,TRUE)
    # else:
    #     familia1 = Padres(nombre,apellido,edad,fecha_nac,TRUE)
    # familia1.save()
    # contexto = {
    #         'Nombre' : nombre,
    #         'Apellido' : apellido
    # } 

    hijo1 = Hijo(nombre="pepe",apellido ="honguito",edad=5,fecha_nac='2017-02-03',es_hijo=True)
    hijo1.save()
    padre = Padres(nombre="Pedro",apellido ="honguito",edad='5',fecha_nac='1980-01-21',es_padre=True)
    padre.save()
    madre = Padres(nombre="Maria",apellido ="honguito",edad='5',fecha_nac='1981-05-05',es_padre=True)
    madre.save()
    contexto = {
        "hijo" : hijo1,
        "padre"  :padre,
        "madre" : madre
    }
    return render(request, 'crear_familia.html', contexto)


def ver_familia(request):
    padres = Padres.objects.all()
    hijos = Hijo.objects.all()
    contexto = {
        'padres' : padres,
        'hijos' : hijos
    }
    return render(request, 'ver_familia.html', contexto)


def crear_familia_parm(request,nombre,apellido,edad,padre):
    if padre == 1:
        integrante1 = Padres(nombre=nombre,apellido =apellido,edad=edad,fecha_nac='1980-01-21',es_padre=True)
    else:
        integrante1 = Hijo(nombre=nombre,apellido =apellido,edad=edad,fecha_nac='2018-01-21',es_hijo=True)
    integrante1.save()
    
    #  today =date.today() 
    # edad = today.year-fecha_nac
    # if edad < 18:
    #     familia1 = Hijo(nombre,apellido,edad,fecha_nac,TRUE)
    # else:
    #     familia1 = Padres(nombre,apellido,edad,fecha_nac,TRUE)
    # familia1.save()
    # contexto = {
    #         'Nombre' : nombre,
    #         'Apellido' : apellido
    # } 
    contexto = {
        'integrante' : integrante1
    }
    return render(request, 'crear_familia_parm.html', contexto)