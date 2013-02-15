import os
import cgi

class Productes():
    dic_produ={}
    
    def __init__(self):
        self.llegir_arxiu()
        
    def llegir_arxiu(self):
        fitxer="productes.txt"
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
    
    def captarProductes(self):
        formulari=self.agafarProductes()
        dic_form={}
        for Nom,Stock,Preu in formulari
            quantitat=request.[Nom]
            dic_form.update({ID:{'Nom':Nom, 'Stock':quantitat, 'Preu':Preu}})
        return dic_form
        

    def introduirDades(dadesRecollides):
        arxiu = open("comanda.txt","a")
        for local in resultats.keys():
            for visitant in resultats[local].keys():
                arxiu.write("%s/%s/%s/%s\n" % (str(local),str(visitant),str(resultats[local][visitant]._gols_local),str(resultats[local][visitant]._gols_visit)))
        arxiu.close()
        return True

