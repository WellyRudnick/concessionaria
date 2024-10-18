class Veiculo():
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.ano} {self.cor}'