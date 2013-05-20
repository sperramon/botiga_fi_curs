import os
import cgi
here = os.path.dirname(os.path.abspath(__file__))
class Producte():
    identificador_compra=0
    identificador=0
    nom="defecte"
    stock=0
    preu=0
    
    def __init__(self):
        pass
    
    def establir_identificador(self,identificador):
        self.identificador=identificador
        
    def agafar_identificador(self):
        return self.identificador
        
    def establir_nom(self,nom):
        self.nom=nom
        
    def agafar_nom(self):
        return self.nom
        
    def establir_stock(self,stock):
        self.stock=stock
                
    def agafar_stock(self):
        return self.stock
        
    def establir_preu(self,preu):
        self.preu=preu
                
    def agafar_preu(self):
        return self.preu
        
    def establir_identificador_compra(self,identificador_compra):
        self.identificador_compra=identificador_compra
                
    def agafar_identificador_compra(self):
        return self.identificador_compra

def llegir_arxiu():
        fitxer=here+"/productes.txt"
        llistaRecollida=[]
        if(comprovar_arxiu(fitxer)):
            arxiu=open(fitxer,'r')
            for linia in arxiu:
                linia=linia.rstrip()
                Id,Nom,Stock,Preu=linia.split('/')
                nouProducte=Producte()
                nouProducte.establir_identificador(Id);
                nouProducte.establir_nom(Nom);
                nouProducte.establir_stock(Stock);
                nouProducte.establir_preu(Preu);
                llistaRecollida.append(nouProducte);
            arxiu.close()
            return llistaRecollida
        else:
            print("No s'ha trovat l'arxiu")
            return 0
        
def comprovar_arxiu(arxiu):
    if os.path.exists(arxiu):
        return 1
    else:
        return 0

def captarProductes(request):
    llistaRecollida=llegir_arxiu()
    recorrerLlista=0;
    for identificador in request.POST:
        if(request.POST[identificador]!="Finalitzar comanda"):
            quantitat=request.POST[identificador];
            if(quantitat.isdigit()):
                llistaRecollida[recorrerLlista].establir_stock(quantitat);
        recorrerLlista=recorrerLlista+1;
    introduirDades(llistaRecollida);
    return llistaRecollida
    

def introduirDades(llistaRecollida):
    fitxer2=here+"/numerocomanda.txt"
    arxiu2 = open(fitxer2,"r");
    for linia2 in arxiu2:
        numeroComanda=linia2
    numeroFitxer=int(numeroComanda)+1;
    arxiu2.close()
    
    # si no ho feia d'aquesta manera no podia llegir i despres guardar valors..'
        
    fitxer2=here+"/numerocomanda.txt"
    arxiu2 = open(fitxer2,"w+");
    arxiu2.write("%s" % (numeroFitxer));
    arxiu2.close()
    #
    
    fitxer=here+"/comanda.txt"
    arxiu = open(fitxer,"a+");
    for x in llistaRecollida:
        quantitat=x.agafar_stock();
        if(quantitat.isdigit()):
            if(quantitat=="0"):
                pass
            else:
                arxiu.write("%s/%s/%s/%s/%s\n" % (numeroComanda,x.agafar_identificador(),x.agafar_nom(),x.agafar_stock(),x.agafar_preu()));
    arxiu.close()
    
def llegirComanda():
    fitxer=here+"/comanda.txt"
    llistaRecollida=[]
    if(comprovar_arxiu(fitxer)):
        arxiu=open(fitxer,'r')
        for linia in arxiu:
            linia=linia.rstrip()
            Identificador_compra,Id,Nom,Stock,Preu=linia.split('/')
            nouProducte=Producte()
            nouProducte.establir_identificador_compra(Identificador_compra);
            nouProducte.establir_identificador(Id);
            nouProducte.establir_nom(Nom);
            nouProducte.establir_stock(Stock);
            nouProducte.establir_preu(Preu);
            llistaRecollida.append(nouProducte);
        arxiu.close()
        return llistaRecollida
    else:
        print("No s'ha trovat l'arxiu")
        return 0
