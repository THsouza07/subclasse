class Moto():
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca,modelo)
        self.cilindrada = cilindrada

    def empinar(self):
        print(f"{self.marca} {self.modelo} empinou e caiu.")    
