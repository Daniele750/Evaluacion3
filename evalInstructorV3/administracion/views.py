import os
import hashlib
import sqlite3 as sql3
from datetime import datetime, date, timedelta
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from evalinstructor.utils import *
from dbs.dbs import *

BASE_DIR = settings.BASE_DIR
timing = datetime.today().date()


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('administracion')
        else:
            messages.info(request, f'Algo no salio bien, Intentelo otra vez')
            return redirect('/')
    context = {"title": "LogIn"}
    return render(request, "administracion/login.html", context)


def userLogout(request):
    logout(request)
    return redirect('/')


def administracion(request):
    try:
        sqlQuery = f"""SELECT * FROM Coordinadores"""
        coordinaciones = call_db(sqlQuery)
        startdate = datetime.strptime(coordinaciones[0][6], '%Y-%m-%d %H:%M:%S')
        endCoordination = startdate + timedelta(days=15)
        endInstPhoto = startdate + timedelta(days=22)
        endEvaluation = startdate + timedelta(days=38)
        context = {'title':'Administracion', 
                    'coordinaciones':coordinaciones, 
                    'startdate':startdate, 
                    'endCoordination':endCoordination, 
                    'endInstPhoto':endInstPhoto,
                    'endEvaluation':endEvaluation }
        return render(request, 'administracion/administracion.html', context)
    except:
        context = {'title': 'Administracion'}
        return render(request, 'administracion/administracion.html', context)
