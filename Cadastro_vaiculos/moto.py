from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, km_rodados, cilindradas):
        super().__init__(marca, modelo, ano, km_rodados)
        self._cilindradas = cilindradas

    def calcular_ipva(self, valor_mercado):
        return valor_mercado * 0.02

    def get_cilindradas(self):
        return self._cilindradas
