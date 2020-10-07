#!/bin/bash

function Practica(){
for i in $(ls);
do
   a=$i
   if [ "Practica3_Bash.sh" == "$a" ]; then
       echo "El Archivo $a si se encuentra"
   fi
done
}
echo "----Lista de archivos----"
ls | sort

Practica
