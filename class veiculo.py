class veiculo:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.frear = False

    def __string__(self):
        estado = "freado" if self.freando else "acelerando"
        return f'''Marca: {self.marca}
        Modelo: {self.modelo} 
        Estado: {estado} 
'''
    def frear(self):
        if not self.freando:
            self.frear = True
            print(f'O seu {self.marca} acelerou')
        else:         
            print(f'O seu {self.marca} está acelerando')

    def acelerar(self):
        if self.acelerando:
            self.acelerar = False
            print(f'O seu {self.marca} acelerou!')
        else:
            print(f'O seu {self.marca} já está acelerando.') 

meu_veiculo = veiculo(marca="honda", modelo="hornet")
print(meu_veiculo)  
meu_veiculo.frear()  
meu_veiculo.acelerar()    
                 
    
    
 

        
            

