<html>
    <head>
    </head>
   <body>
         <a href="/"/>Tornar a l'inici</a>
      <h1>Comandes</h1>
    <table border='1'>
      <tr><td>Identificador Compra</td><td>Id del producte</td><td>Nom</td><td>Stock</td><td>Preu</td><td>Total</td></tr>
      % for x in productes:
        <%
            iden_compra=x.agafar_identificador_compra()
            iden=x.agafar_identificador()
            nom=x.agafar_nom()
            stock=x.agafar_stock()
            preu=x.agafar_preu()
            total=float(preu)*float(stock);
        %>
         <tr><td>${iden_compra}</td><td>${iden}</td><td>${nom}</td><td>${stock}</td><td>${preu}</td><td>${total}&euro;</td></tr>
      % endfor
   </table>
   </body>
</html>

