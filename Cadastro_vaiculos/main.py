from carro import Carro
from moto import Moto
from caminhao import Caminhao

def cadastrar_veiculo():
    tipo = input("\nInforme o tipo de veículo (carro, moto ou caminhão): ").lower()

    if tipo not in ["carro", "moto", "caminhão", "caminhao"]:
        print("Tipo de veículo inválido")
        return
    
    marca = input("Informe a marca do veículo: ")
    modelo = input("Informe o modelo do veículo: ")
    ano = int(input("Informe o ano do veículo: "))
    km_rodados = int(input("Informe a quilometragem rodada do veículo: "))
    valor_mercado = float(input("Informe o valor de mercado do veículo: "))

    if tipo == "carro":
        num_portas = int(input("Informe o número de portas do veículo: "))
        veiculo = Carro(marca, modelo, ano, km_rodados, num_portas)
    elif tipo == "moto":
        cilindradas = int(input("Informe a cilindrada da moto: "))
        veiculo = Moto(marca, modelo, ano, km_rodados, cilindradas)
    elif tipo == "caminhão" or tipo == "caminhao":
        capacidade_carga = float(input("Informe a capacidade de carga do caminhão: "))
        veiculo = Caminhao(marca, modelo, ano, km_rodados, capacidade_carga)

    ipva = veiculo.calcular_ipva(valor_mercado)

    print()
    layout(km_rodados, valor_mercado)
    print("Veículo cadastrado com sucesso!")
    layout(km_rodados, valor_mercado, simbolo="-")
    print(f"Marca: {veiculo.get_marca()}")
    print(f"Modelo: {veiculo.get_modelo()}")
    print(f"Ano: {veiculo.get_ano()}")
    print(f"Quilometragem rodada: {veiculo.get_km_rodados():,.0f}".replace(",", "X").replace(".", ",").replace("X", ".") + " Km")
    print(f"Valor de mercado: R$ {valor_mercado:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    if tipo == "carro":
        print(f"Número de portas: {veiculo.get_num_portas()}")
    elif tipo == "moto":
        print(f"Cilindradas: {veiculo.get_cilindradas()} cc")
    elif tipo == "caminhão" or tipo == "caminhao":
        print(f"Capacidade de carga: {veiculo.get_capacidade_carga():,.0f}".replace(",", "X").replace(".", ",").replace("X", ".") + " Kg")

    print(f"IPVA: R$ {ipva:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    layout(km_rodados, valor_mercado, simbolo="-")
    layout(km_rodados, valor_mercado)

def layout(km_rodados, valor_mercado, simbolo="*"):
    if km_rodados >= 1000000 or valor_mercado >= 1000000:
        print(simbolo * 35)
    else:
        print(simbolo * 33)

if __name__ == "__main__":
    while True:
        cadastrar_veiculo()
        continuar = input("\nDeseja cadastrar outro veículo? (s/n): ").lower()
        if continuar != "s":
            break
