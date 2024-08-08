import os
import sqlite3 as sql3
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from dbs.dbs import call_db, call_db_one

BASE_DIR = settings.BASE_DIR


def home(request):
    end_date = []
    sqlQuery = f"""SELECT * FROM Coordinadores"""
    try:
        coordinaciones = call_db(sqlQuery)
        end_date = coordinaciones[0][6]

        context = {"title": "SENA - Evaluación de instructores", "end_date": end_date}
        return render(request, "evalinstructor/home.html", context)
    except:
        messages.warning(request, f'No se encontro la Base de Datos')
        context = {"title": "Subir Archivo de Activación"}
        return render(request, "loadlists/loadActivation.html", context)


def validarHash(request):
    if request.method == 'POST':
        hash = request.POST.get('hash')
        
            # Coordinacion
        sqlQuery = f"""SELECT * FROM Coordinadores WHERE HASH =?"""
        theOne = call_db_one(sqlQuery, hash)
        if theOne[8] == 'coordinador':

            context = {"title": "Subir Listas", "theOne":theOne}
            return render(request, "loadlists/loadings.html", context)
        else:
            print('coordinador', "NONE")


        sqlQuery = f"""SELECT * FROM instructores WHERE HASH =?"""
        theOne = call_db_one(sqlQuery, hash)
        if theOne[8] == 'instructores':

            context = {"title": "Subir Listas", "theOne":theOne}
            return render(request, "loadlists/fotoup.html", context)
        else:
            print('instructores', "NONE")
    
    return HttpResponse(theOne)
