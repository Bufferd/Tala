#!/bin/bash
clear
echo "Content-type: text/html"
echo 
#Listar as categoras existentes

validacao(){

dir="/var/www/html/Invent-rio/listar.html/"
cd $dir

if [[ -r $1 ]]
	then
		echo
	else
		listar
	fi
}


listar(){
#clear

read Entre com a sua categoria:
<input type="text" name="categoria"> CATEGORIA

if [[ $CATEGORIA == 0 ]]
	then
		dir="/home/vinicius/Projeto/Invent-rio/"
		cd $dir
		source menu.sh
	fi

cd /home/vinicius/Projeto/Invent-rio/registros/

validacao $CATEGORIA

cd /home/vinicius/Projeto/Invent-rio/registros/$CATEGORIA/

arquivo="$CATEGORIA.csv"
less $arquivo

#less $CATEGORIA.csv
clear
listar
}

listar
