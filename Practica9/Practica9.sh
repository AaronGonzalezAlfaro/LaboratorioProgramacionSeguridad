#!/bin/bash

echo "Ingrese el Mensaje que quiera enviar: "
read a

echo "Nombre de la Lista de Correos (TXT): "
read c


cat $c | xargs -I {} python Practica9.py -a {} -m "$a"
