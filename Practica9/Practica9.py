#!/usr/bin/env python3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import argparse

parser = argparse.ArgumentParser(description = 'Manda Mensajes a Multiples Correos')
parser.add_argument('-a', '--a', help='Lista de Correos a Enviar el Mensaje')
parser.add_argument('-m', '--m', help='Mensaje a Mandar')
args = parser.parse_args()

correo = args.a
message = args.m
correo = str(correo)
message = str(message)


data = {}
with open('pass.json') as f:
        data = json.load(f)
# create message object instance
msg = MIMEMultipart()

#message = "Ciaoo!"

# setup the parameters of the message
msg['From'] = data['user']

msg['To'] = correo
msg['Subject'] = "Buenos Dias/Tardes/Noches"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

#create server
server = smtplib.SMTP('smtp.office365.com:587')
server.starttls()

# Login Credentials for sending the mail
print(data['user'])
server.login(data['user'], data['pass'])

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print("successfully sent email to %s:" % (msg['To']))
