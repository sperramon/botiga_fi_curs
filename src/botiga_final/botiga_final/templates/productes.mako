<html>
    <head>
     <script language="Javascript">
        llista=new Array();
           
       function llistar(lloc){
        var valor=document.getElementById(lloc).value;
            if(valor>0){
            var stock = llista.indexOf(lloc); // comprovem els productes introduits si hi ha alguna coincidencia
            stock > -1 && llista.splice(llista,1); // Eliminem l'stock que hi hagi ja introduit  -- revisar
            llista.push("<br/>"+lloc+":"+valor+"");
            document.getElementById("cistella").innerHTML=llista;
            }
        }
        
        function suma(lloc){
        var valor=document.getElementById(lloc).value;
        valor++;
        document.getElementById(lloc).value=valor; 
            
        }
        
        function resta(lloc){
        var valor=document.getElementById(lloc).value;
            if(valor>0){        
            valor--;
            document.getElementById(lloc).value=valor;
            }
        }
        
       </script>
    </head>
   <body>
      
      <h1>Botigueta</h1>
      <form name="formulari" method="POST">
      % for prod in productes:
         <table border='1'>
         <tr><td>Producte:</td><td>${productes[prod]["Nom"]}</td></tr>
         <tr><td>Stock:</td><td>${productes[prod]["Stock"]}</td></tr>
         <tr><td>Preu:</td><td>${productes[prod]["Preu"]}</td></tr>
         <% nom = productes[prod]["Nom"] %>
         <tr>
             <td><input type='text' value='0' name="${nom}" id="${nom}" size='2' disabled/>
             <input type='button' value='Afegir' name='afegir' id='afegir' onClick="llistar('${nom}');"/></td>
             <td><input type='button' value='+' name='sumar' id='sumar' onClick="suma('${nom}');"/>
             <input type='button' value='-' name='restar' id='restar' onClick="resta('${nom}');"/></td></tr>
         </table>
         <br/><br/>
         <input type="submit" value="Finalitzar Comanda" name="acabar" id="acabar"/>
      % endfor
   </form>
   <div id='cistella' name='cistella'>Comanda</div>
   </body>
</html>

