class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas, valor_mercado):
        super().__init__(marca, modelo, ano)
        self._num_portas = num_portas
        self._valor_mercado = valor_mercado

    def num_portas(self):
        return self._num_portas

    def num_portas(self, valor):
        self._num_portas = valor

    def valor_mercado(self):
        return self._valor_mercado

    def valor_mercado(self, valor):
        self._valor_mercado = valor

    def calcular_ipva(self):
        return self._valor_mercado * 0.04


print(f"IPVA do carro: R${Carro.calcular_ipva():.2f}")