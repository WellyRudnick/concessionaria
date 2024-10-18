class Veiculo():

    def __init__(self, modelo, marca, ano, valor_mercado):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.valor_mercado = valor_mercado

    # Métodos responsáveis por retornar os atributos dos veículos
    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo

    def getAno(self):
        return self.ano
    
    def getValor(self):
        return self.valor_mercado