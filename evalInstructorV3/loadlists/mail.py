import os
import json
from datetime import datetime, date, timedelta
from django.conf import settings
from django.http import HttpResponse

from django.core.mail import send_mail
from dbs.dbs import *

with open("static/docs/evalins.json") as config_file:
    config = json.load(config_file)


def sendMailCoordinaciones():
    sqlQuery1 = f"""SELECT * FROM Coordinadores"""
    sqlQuery2 = f"""SELECT * FROM EvalFechas"""
    coordinaciones = call_db(sqlQuery1)
    evalFechas = call_db(sqlQuery2)

    dates = {'startdate':evalFechas[0][0], 'endCoordination':evalFechas[0][1], 'endInstPhoto':evalFechas[0][2], 'endEvaluation':evalFechas[0][3]}

    for i in coordinaciones:
        mailData = {'startdate':evalFechas[0][0], 'endCoordination':evalFechas[0][1], 'endInstPhoto':evalFechas[0][2], 'endEvaluation':evalFechas[0][3],
                    'REGIONAL': i[0], 'CENTRO': i[1], 'COORDINACION': i[2], 'NOMBRE': i[3], 'APELLIDOS': i[4], 'CORREO_COORDINADOR': i[5], 'HASH': i[7],
                    'subject': "Activacion del Aplicativo para Evaluar a los Instructores"}

            # SEND EMAIL
        message = '''
        Señor(a) Coordinador(a) {} {}
        Regional: {}, Centro Educativo: {}, Coordinación: {}

        Con el presente le solicitamos atentamente subir a la plataforma los listados de Instructores y Aprendices de las áreas a evaluar.

        El ingreso a la plataforma es en "www.datasena.evalinstructor.com" y su HASH para el acceso es:
        
        {}

        Las fechas de esta temporada de evaluación son las siguientes:
        >> Fechas para que las coordinaciones suban las listas de aprendices e instructores:
        Fecha de Inicio {} - Fecha Limite {}
        >> Fecha Limite para que los instructores suban su foto:
        Fecha de Inicio {} - Fecha Limite {}
        >> La evaluación por parte de los aprendices se realizara:
        Fecha de Inicio {} - Fecha Limite {}

        Agradecemos la pronta gestión de los listados requeridos.
        
        Si tiene algunas dudas o sugerencias por favor comunicarse con la subdirección de su centro educativo

        Atentamente

        Centro De Producción De Soluciones Inteligentes
        Centro de Gestión de Mercados, Logística y Tecnologías de la Información.
        '''.format(mailData['NOMBRE'], mailData['APELLIDOS'], 
                    mailData['REGIONAL'], mailData['CENTRO'], mailData['COORDINACION'], 
                    mailData['HASH'], 
                    mailData['startdate'], mailData['endCoordination'], 
                    mailData['endCoordination'], mailData['endInstPhoto'], 
                    mailData['endInstPhoto'], mailData['endEvaluation'])

        send_mail(mailData['subject'], message, '', [mailData['CORREO_COORDINADOR']])

    return


def sendMailInstructor():
    sqlQuery1 = f"""SELECT * FROM Instructores"""
    sqlQuery2 = f"""SELECT * FROM EvalFechas"""
    instructores = call_db(sqlQuery1)
    evalFechas = call_db(sqlQuery2)

    dates = {'startdate':evalFechas[0][0], 'endCoordination':evalFechas[0][1], 'endInstPhoto':evalFechas[0][2], 'endEvaluation':evalFechas[0][3]}

    for i in coordinaciones:
        mailData = {'startdate':evalFechas[0][0], 'endCoordination':evalFechas[0][1], 'endInstPhoto':evalFechas[0][2], 'endEvaluation':evalFechas[0][3],
                    'REGIONAL': i[0], 'CENTRO': i[1], 'COORDINACION': i[2], 'NOMBRE': i[3], 'APELLIDOS': i[4], 'CORREO_COORDINADOR': i[5], 'HASH': i[7],
                    'subject': "Activacion del Aplicativo para Evaluar a los Instructores"}

            # SEND EMAIL
        message = '''
        Señor(a) Instructor(a) {} {}
        Regional: {}, Centro Educativo: {}, Coordinacion: {}

        La plataforma para que los aprendices den apreciaciones sobre su estilo de enseñanza ha sido activada y le solicitamos muy amablemente subir una foto de su rostro reciente y de frente con la finalidad que los aprendices no tengan dudas sobre su identidad.

        El ingreso a la plataforma es en "www.datasena.evalinstructor.com" y su HASH para el acceso es:
        
        {}

        Las fechas de esta temporada de evaluación son las siguientes:
        >> Fecha Limite para que los instructores suban su foto:
        Fecha de Inicio {} - Fecha Limite {}
        >> La evaluación por parte de los aprendices se realizara:
        Fecha de Inicio {} - Fecha Limite {}

        Agradecemos la pronta gestión al requerimiento.
        
        Si tiene algunas dudas o sugerencias por favor comunicarse con la coordinación de su centro educativo

        Atentamente

        Centro De Producción De Soluciones Inteligentes
        Centro de Gestión de Mercados, Logística y Tecnologías de la Información.
        '''.format(mailData['NOMBRE'], mailData['APELLIDOS'], 
                    mailData['REGIONAL'], mailData['CENTRO'], mailData['COORDINACION'], 
                    mailData['HASH'], 
                    mailData['endCoordination'], mailData['endInstPhoto'], 
                    mailData['endInstPhoto'], mailData['endEvaluation'])

        send_mail(mailData['subject'], message, '', [mailData['CORREO_COORDINADOR']])

    return
