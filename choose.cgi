#!/bin/bash
read STRING
OPCAO=$(echo $STRING | cut -d"=" -f2)
red(){
	source redirecionandol.cgi ../cadastrarpatri.html
}
echo "content-type: text/html"
echo
[[ $OPCAO == "1" ]] && red || echo $OPCAO

#case $OPCAO in
#	1) red ;;
#	2) source adicionar_eq.html ;;
#	3) source editar.html ;;
#       4) source excluir.html ;;
#        5) source excluir_pat.html ;;
 #       6) source novo.html ;;
  #      8) source deslogar.html ;;
   #     *) invalido ; menu ;;
#esac
#
