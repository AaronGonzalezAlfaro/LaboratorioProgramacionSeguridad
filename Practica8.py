#!/usr/bin/env python3

import ftplib
import argparse
#from ftplib import FTP, FTP_PORT

#-------------------------------------------------------------------
#El programa surgio un error al final, pero si gaurda lo encontrado.
#-------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Encontrar archivos de Texto - FTP')
parser.add_argument('-enlace', '--enlace', type=str, metavar='', help='Enlace o Link del servidor FTP')
args=parser.parse_args()

serv = args.enlace
if(serv == None):
    serv = 'ftp.us.debian.org'
    
def rec():

    lista = ftp.nlst()
    archivos = []
    ftp.retrlines('LIST', archivos.append)
    for i in lista:
        if(archivos[lista.index(i)].startswith('dr')) or \
          (archivos[lista.index(i)].startswith('l')):
            try:
                #Primeros Dos Comandos por si quiere ver los Directorios o los simbolicos
                #print("Directorio: ", i)
                #print("Elemento: ", archivos[lista.index(i)])
                ftp.cwd(i)
                rec()
            except:
                a = 1
        else:
            #print("Else", i)
            if(i.startswith == "README" or i.endswith('.txt') \
               or i.endswith('.msg') or i == 'README'):
                print("Archivo: ", i)
                with open(i, 'wb') as fp:
                    ftp.retrbinary('RETR ' + i, fp.write)
    ftp.cwd("..")

def connect_ftp(server, user, mail):
    global ftp
    ftp = ftplib.FTP(server, user, mail)
    rec()
    ftp.quit()

if __name__ == '__main__':
    connect_ftp(server=serv, user='anonymous', mail='nobody@nourl.com')

