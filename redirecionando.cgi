#!/bin/bash
cat <<EOF
<html>
<title>Redirecionando...</title>
<head>
<meta http-equiv="refresh" content=1;url="../$1">
</head>
<h1>Redirecionando...!</h1>
</html>
EOF
