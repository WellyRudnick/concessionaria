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

    # Métodos responsáveis por alterar os atributos dos veículos
    def setMarca(self, marca):
        self.marca = input('Informe a marca do veículo: ')
    
    def setModelo(self, modelo):
        self.modelo = input('Informe o modelo do veículo: ')

    def setAno(self, ano):
        self.ano = int(input('Informe o ano do veículo: '))

    def setValor(self, valor_mercado):
        self.valor_mercado = float(input('Informe o valor do veículo: '))