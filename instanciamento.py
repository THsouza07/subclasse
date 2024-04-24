if __name__ == '__main__':
    carro1 = Carro("Porsche", "boxster", "branca")
    print(carro1.marca, carro1.modelo)
    carro1.abrir_porta()

    moto1 = Moto("Honda", "Hornet", "600")
    print(moto1.marca, moto1.modelo, moto1.cilindrada)
    moto1.empinar()