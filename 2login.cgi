#!/bin/bash
read STRING
falhou(){
	echo "<h1> Falhou </h1>"
	echo "<a href="../1index.html"> Voltar... </a>"
}
passou(){
	source redirecionando.cgi 3menu.html
}
USER=$(echo $STRING | cut -d"&" -f1 | cut -d"=" -f2)
PASS=$(echo $STRING | cut -d"&" -f2 | cut -d"=" -f2)
USUARIO=$(grep "^$USER;" 'senha.pwd' | cut -d";" -f1)
SENHA=$(grep "^$USER;" 'senha.pwd' | cut -d";" -f2)
echo "content-type: text/html"
echo
[[ $USER == $USUARIO ]] && [[ $PASS == $SENHA ]] && passou || falhou
