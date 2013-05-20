<html>
    <head>
     <script language="Javascript">
        llista=new Array();
           
       function llistar(lloc){
        var valor=document.getElementById(lloc).value;
            if(valor>0){
            llista.push("<br/>"+lloc+":"+valor+"");
            document.getElementById("cistella").innerHTML=llista;
            }
        }
        
        function suma(lloc,limit){
        var valor=document.getElementById(lloc).value;
        if(valor!=limit){
            valor++;
            document.getElementById(lloc).value=valor; 
            }
        }
        
        function resta(lloc,limit){
        var valor=document.getElementById(lloc).value;
            if(valor>0){        
            valor--;
            document.getElementById(lloc).value=valor;
            }
        }
        
       </script>
    </head>
   <body>
      <a href="/"/>Tornar a l'inici</a>
      <h1>Botigueta</h1>
      <form name="formulari" method="POST" action="${request.route_url('fercomanda')}">
      % for x in productes:
        <% 
            iden=x.agafar_identificador()
            nom=x.agafar_nom()
            stock=x.agafar_stock()
            preu=x.agafar_preu()
         %>
         <table border='1'>
         <tr><td>Producte:</td><td>${nom}</td></tr>
         <tr><td>Stock:</td><td>${stock}</td></tr>
         <tr><td>Preu:</td><td>${preu}</td></tr>
         <tr>
             <td><input type='text' value='0' name="${nom}" id="${nom}" />
             <input type='button' value='Afegir' name='afegir' id='afegir' onClick="llistar('${nom}','${stock}');"/></td>
             <td><input type='button' value='+' name='sumar' id='sumar' onClick="suma('${nom}','${stock}');"/>
             <input type='button' value='-' name='restar' id='restar' onClick="resta('${nom}','${stock}');"/></td></tr>
         </table>
         <br/><br/>
      % endfor
   <input type="submit" value="Finalitzar Comanda" name="acabar" id="acabar"/>
   </form>
   <div id='cistella' name='cistella'>Comanda</div>
   </body>
</html>

