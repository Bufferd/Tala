#!/bin/bash
read POST

foi(){
cat << EOFFF
content-type: text/html

<html>
<h1>oioi</h1>
<a href="../3menu.html">voltar</a>
</html>
EOFFF
}

naofoi(){
cat <<EOFFF
content-type: text/html

<html>
<h1>invalido</h1>
<a href="../3menu.html">voltar</a>
</html>
EOFFF
}

usuario=$(echo $POST | cut -d"&" -f1 | cut -d"=" -f2)
senha=$(echo $POST | cut -d"&" -f2 | cut -d"=" -f2)
if [[ ! $(grep "^$usuario:" senha.pwd) ]] ; then
echo "$usuario:$senha" >> senha.pwd
	foi
else
	naofoi
fi

