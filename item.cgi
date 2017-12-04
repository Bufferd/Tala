<html>
<head>
<meta charset='UTF-8'>
</head>
<body>
Categoria:<br>
  <input type="text" name="produto" placeholder="Computador">
<br><br>
</body>
Descrição:<br>
  <input type="text" name="categoria" placeholder="Periféricos">
 <br><br>
</body>
Nome do ambiente:<br>
 <input type="text" name="localidade" placeholder="SENAI">
 <br><br>	
Apelido:<br>
 <input type="text" name="predio" placeholder="São Paulo">
<br><br>
</body>
</form>
<br>
Quantidade:<br>
<form action="/ok.html" method="post">
<input type="text" name="item" placeholder="">
<br><br>
<input type="submit" value="Quantidade">
 <br><br>
<a href="/3menu.html">Voltar...</a>
</body>
</html>

read POST
foi(){
cat << EOFFF
content-type: text/html
 
<html>
<h1>oioi</h1>
<a href="../3menu.html">voltar</a>
</html>
EOFFF


naofoi(){
cat <<EOFFF
content-type: text/html
 
<html>
  oi</h1>
   10 <a href="../3menu.html">voltar</a>
  </html>
   EOFFF
}
cadastro=$(echo $POST | cut -d"&" -f1 | cut -d"=" -f2)
if [[ ! $("$cadastro"  ]] ; then
echo "$usuario:$senha" >> senha.pwd
         foi
else
       naofoi
fi

         
