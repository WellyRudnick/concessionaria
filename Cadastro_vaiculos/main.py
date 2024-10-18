class Veiculo():
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.ano} {self.cor}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, portas):
        super().__init__(marca, modelo, ano, cor)
        self.portas = portas

    def __str__(self):
        return f'{super().__str__()} {self.portas} portas'