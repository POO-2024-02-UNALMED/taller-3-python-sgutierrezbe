class tv:
    numTV = 0 

    def __init__(self, marca, estado, control):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = control
        TV.numTV += 1 

        
    def setMarca(self, marca):  
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control
    
    def setPrecio(self, precio):
        self.precio = precio
    
    def getPrecio(self):
        return self.precio
    
    def setCanal(self, canal):
         self.canal = canal

    def getCanal(self):
        return self.canal

    def setVolumen(self, volumen):
        self.volumen = volumen  
    
    def getVolumen(self):
        return self.volumen
    
    @classmethod
    def getNumTV(cls):
        return cls.numTV
