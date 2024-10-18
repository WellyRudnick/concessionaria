class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, valor_mercado, cilindradas):
        super().__init__(marca, modelo, ano, valor_mercado)
        self.cilindradas = cilindradas

    def cilindradas(self):
        return self.cilindradas

    def cilindradas(self, valor):
        self.cilindradas = valor

    def calcular_ipva(self):
        return self.valor_mercado * 0.02
