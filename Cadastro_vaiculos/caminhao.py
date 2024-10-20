from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, km_rodados, capacidade_carga):
        super().__init__(marca, modelo, ano, km_rodados)
        self._capacidade_carga = capacidade_carga

    def calcular_ipva(self, valor_mercado):
        return valor_mercado * 0.015

    def get_capacidade_carga(self):
        return self._capacidade_carga
