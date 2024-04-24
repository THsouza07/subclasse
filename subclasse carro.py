class carro():
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def abrir_porta(self):
        print(f"{self.marca} {self.modelo} porta aberta")    
