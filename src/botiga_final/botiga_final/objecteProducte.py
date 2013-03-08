import os
import cgi
here = os.path.dirname(os.path.abspath(__file__))
class Productes():
    dic_produ={}
    
    def __init__(self):
        self.llegir_arxiu()
        
    def llegir_arxiu(self):
        fitxer=here+"/productes.txt"
        if(self.comprovar_arxiu(fitxer)):
            arxiu=open(fitxer,'r')
            diccionari={}
            for linia in arxiu:
                linia=linia.rstrip()
                ID,Nom,Stock,Preu=linia.split('/')
                diccionari.update({ID:{'Nom':Nom, 'Stock':Stock, 'Preu':Preu}})
            arxiu.close()
            self.dic_produ=diccionari
            return 1
            
        else:
            print("No s'ha trovat l'arxiu")
            return 0
        
    def comprovar_arxiu(self,arxiu):
        if os.path.exists(arxiu):
            return 1
        else:
            return 0

    def agafarProductes(self):
        return self.dic_produ
    
    def captarProductes(self,request):
        self.llegir_arxiu()
        formulari=self.agafarProductes()
        dic_form={}
        for Nom,Stock,Preu in formulari:
            quantitat=request.POST.get(Nom);
            dic_form.update({ID:{'Nom':Nom, 'Stock':quantitat}});
        return dic_form
        

    def introduirDades(self,dadesRecollides):
        fitxer=here+"/comanda.txt"
        arxiu = open(fitxer,"a+");
        if(self.comprovar_arxiu(arxiu)):
            for Nom,Stock,Preu in dadesRecollides.keys():
                arxiu.write("%s/%s/%s\n" % (Nom,Stock,Preu));
            arxiu.close()
            return True
        else:
            print("No s'ha pogut escriure a l'arxiu'")
            return 0

    def llegir_comanda(self):
        fitxer=here+"/comanda.txt"
        if(self.comprovar_arxiu(fitxer)):
            arxiu=open(fitxer,'r')
            diccionari={}
            for linia in arxiu:
                linia=linia.rstrip()
                ID,Nom,Stock,Preu=linia.split('/')
                diccionari.update({ID:{'Nom':Nom, 'Stock':Stock, 'Preu':Preu}})
            arxiu.close()
            self.dic_produ=diccionari
            return 1
            
        else:
            print("No s'ha trovat l'arxiu")
            return 0
