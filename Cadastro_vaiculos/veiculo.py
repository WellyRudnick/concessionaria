from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, km_rodados):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._km_rodados = km_rodados

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_ano(self):
        return self._ano

    def set_ano(self, ano):
        self._ano = ano

    def get_km_rodados(self):
        return self._km_rodados

    def set_km_rodados(self, km_rodados):
        self._km_rodados = km_rodados

    @abstractmethod
    def calcular_ipva(self, valor_mercado):
        pass
