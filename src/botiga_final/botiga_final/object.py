class Producte():
    _id=None
    _nom=None
    _stock=None
    _preu=None
    
    def __init__(self):
        self._id=0
        self._nom=""
        self._stock=0
        self._preu=0
    
    def agafar_id(self):
        return self._id
    
    def establir_id(self,valor):
        self._id=valor
        
    def agafar_nom(self):
        return self._nom
    
    def establir_nom(self,valor):
        self._nom=valor
    
    def agafar_stock(self):
        return self._stock
    
    def establir_stock(self,valor):
        self._stock=valor
        
    def agafar_preu(self):
        return self._preu
    
    def establir_preu(self,valor):
        self._preu=valor
        
    def llegir_arxiu(fitxer):
        if(comprovar_arxiu(fitxer)):
            arxiu=open(fitxer,'r')
            diccionari={}
            
            for linia in arxiu:
                linia=linia.rstrip()
                ID,Nom,Stock,Preu=linia.split('/')
                material[Nom]=Dades_Productes()
                material[Nom].establir_id(ID)
                material[Nom].establir_nom(Nom)
                material[Nom].establir_stock(Stock)
                material[Nom].establir_preu(Preu)
            arxiu.close()
            return 1
        else:
            print("No s'ha trovat l'arxiu")
            return 0

    def comprovar_arxiu(arxiu):
        if os.path.exists(arxiu):
            return 1
        else:
            return 0
    def getProducte(self):
        return diccionari
        
