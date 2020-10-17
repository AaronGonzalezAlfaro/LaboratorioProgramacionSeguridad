#!/bin/bash


while true; do
    echo "---------MENU---------"
    echo "[1] Codificar "msg.txt""
    echo "[2] Codificar "fcfm.png""
    echo "[3] Decodificar "mystery_img1.txt""
    echo "[4] Decodificar "mystery_img2.txt""
    echo "[0] Salir"
    read -p "Elija una opcion: " op
    case $op in
         [1]* ) codm="$(cat msg.txt | base64)"
		echo "Mensaje Codificado En Base64: " $codm
		codm="$(cat msg.txt | md5sum)"
		echo "Mensaje Codificado en md5sum: " $codm 
		read -p "Presione Enter Para Continuar......" c
		clear
	    ;;
         [2]* ) codi="$(cat fcfm.png | base64)"
		echo "Imagen Codificada en Base 64: " $codi
		codi="$(cat fcfm.png | md5sum)"
		echo "Imagen Codificada en md5sum: " $codi
		read -p "Presione Enter Para Continuar......" c
		clear 
	    ;;
         [3]* ) dec1="$(cat mystery_img1.txt | base64 --decode > Imagen_Mis1.jpg)"
		echo "Imagen decodificada con el nombre "Imagen_Mis1" en su carpeta" $dec1
		dec1="$(cat mystery_img1.txt | md5sum)"
		echo "Imagen Codificada en md5sum: " $dec1
		read -p "Presione Enter Para Continuar......" c
		clear
	    ;;
         [4]* ) dec2="$(cat mystery_img2.txt | base64 --decode > Imagen_Mis2.jpg)"
		echo "Imagen decodificada con el nombre "Imagen_Mis2" en su carpeta" $dec2
		dec2="$(cat mystery_img2.txt | md5sum)"
		echo "Imagen Codificada en md5sum: " $dec2
		read -p "Presionar Enter Para Continuar......" c
		clear
	    ;;
         [0]* ) break;;
         *) echo "Opcion No Encontrada"
	    echo " ";;
    esac
done
