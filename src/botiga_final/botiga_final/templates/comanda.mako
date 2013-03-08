<html>
    <head>
    </head>
   <body>
         
      <h1>Comandes</h1>
      <tr><td>Producte<td><td>Stock<td><td>Preu<td></tr>
      % for prod in productes:
         <table border='1'>
         <tr><td>${productes[prod]["Nom"]}</td><td>${productes[prod]["Stock"]}</td><td>${productes[prod]["Preu"]}</td></tr>
      % endfor
   </table>
   </body>
</html>

