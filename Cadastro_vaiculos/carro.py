from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, km_rodados, num_portas):
        super().__init__(marca, modelo, ano, km_rodados)
        self._num_portas = num_portas

    def calcular_ipva(self, valor_mercado):
        return valor_mercado * 0.04

    def get_num_portas(self):
        return self._num_portas
