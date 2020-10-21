#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import pandas as pd

def Menu_Datos(url, a):
    pagina=requests.get(url)
    soup=BeautifulSoup(pagina.content, 'html.parser')

    #Equpipos

    eq = soup.find_all('span', class_='hide-mobile')
    equipos=list()
    for i in eq:
        equipos.append(i.text)
        
    #Datos Generales y Separacion de Datos

    pg = soup.find_all('span', class_='stat-cell')
    datos=list()
    numPart=list()
    partidosg=list()
    empate=list()
    partidosp=list()
    golesfav=list()
    golescont=list()
    difdepuntos=list()
    puntos=list()
    for i in pg:
        datos.append(i.text)
    n=0
    for i in datos:
        if(n==8):
            n=0
        if(n==0):
            numPart.append(i)
        elif(n==1):
            partidosg.append(i)
        elif(n==2):
            empate.append(i)
        elif(n==3):
            partidosp.append(i)
        elif(n==4):
            golesfav.append(i)
        elif(n==5):
            golescont.append(i)
        elif(n==6):
            difdepuntos.append(i)
        elif(n==7):
            puntos.append(i)
        n+=1
    s=len(equipos)+1
    tabla=pd.DataFrame({'Equipo': equipos}, index=list(range(1,s)))
    print(tabla)
    while True:
        print("\n[1] Numero de Partitdos\n[2] Partidos Ganados\n[3] Empates\n[4] Partidos Perdidos\n[5] Goles a Favor")
        print("[6] Goles en Contra\n[7] Diferencia de Puntos\n[8]Puntos Totales")
        op=int(input("Opcion: "))
        if(op==1):
            table=pd.DataFrame({'Equipo': equipos, 'Partidos': numPart}, index=list(range(1,s)))
            print(table)
        elif(op==2):
            table=pd.DataFrame({'Equipo': equipos, 'Partidos Ganados': partidosg}, index=list(range(1,s)))
            print(table)           
        elif(op==3):
            table=pd.DataFrame({'Equipo': equipos, 'Empates': empate}, index=list(range(1,s)))
            print(table)
        elif(op==4):
            table=pd.DataFrame({'Equipo': equipos, 'Partidos Perdidos': partidosp}, index=list(range(1,s)))
            print(table)
        elif(op==5):
            table=pd.DataFrame({'Equipo': equipos, 'Goles a Favor': golesfav}, index=list(range(1,s)))
            print(table)
        elif(op==6):
            table=pd.DataFrame({'Equipo': equipos, 'Goles en Contra': golescont}, index=list(range(1,s)))
            print(table)
        elif(op==7):
            table=pd.DataFrame({'Equipo': equipos, 'Diferencia de Puntos': difdepuntos}, index=list(range(1,s)))
            print(table)
        elif(op==8):
            table=pd.DataFrame({'Equipo': equipos, 'Puntos Totales': puntos}, index=list(range(1,s)))
            print(table)
        else:
            print("\nEsta Opcion no esta Disponible :c\n")
            continue
        n=int(input("\n\n[1]Continuar\n[0]Salir\nOpcion: "))
        if(n==1):
            continue
        else:
            while True:
                print("\nAntes de Salir, ¿desea guardar en un archivo los datos generales?")
                d=int(input("[1]Si\n[0]No\nOpcion: "))
                if(d==1):
                    table=pd.DataFrame({'Equipo': equipos, 'Partidos': numPart, 'Partidos Ganados': partidosg, 'Empates': empate, 'Partidos Perdidos': partidosp, 'Goles a Favor': golesfav, 'Goles en Contra': golescont, 'Diferencia de Puntos': difdepuntos, 'Puntos Totales': puntos}, index=list(range(1,s)))
                    table.to_csv('Liga_'+a+'.csv')
                    break
                elif(d==0):
                    break
                else:
                    print("\nOpcion no encontrada")
                    continue
            break
    return 0
    
while True:
    print("---------LIGA MX---------")
    a=int(input("Ingrese el Año del 2010 al 2020: "))
    if(a==2020):
        url='https://www.espn.com.mx/futbol/posiciones/_/liga/mex.1/liga-mx'
        a=str(a)
    elif(a==2010 or a==2011 or a==2012 or a==2013 or a==2014 or a==2015 or a==2016 or a==2017 or a==2018 or a==2019):
        a=str(a)
        url='https://www.espn.com.mx/futbol/posiciones/_/liga/MEX.1/temporada/'+a+'/liga-mx'
    else:
        print("Temporada fuera del rango aceptado")
        continue
    Menu_Datos(url, a)
    a=int(input(("\n¿Desea Salir?\n[1]Seguir Con Otra Temporada\n[0]Salir\n")))
    if(a==1):
        print("\n\n")
        continue
    else:
        break
