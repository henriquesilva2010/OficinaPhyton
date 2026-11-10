
def notaalu():
    print ("Olá, mundo")


def saudacao(nome):
    print(f"Olá {nome})")

saudacao("henrique")
"""1. Conversor de temperatura
Crie uma função chamada converter_temperatura()
que receba uma temperatura em Celsius e retorne o valor convertido para Fahrenheit
e Kelvin
Fórmula: 
Fahrenheit = Celsius × 1,8 + 32.
Kelvin = Celsius + 273.15
No programa principal, peça a temperatura ao usuário e mostre o resultado."""
def graus ():

    converter =float(input("Escreva a temperatura em Celsius:"))

    fahr=converter*1.8 + 32
    kel= (converter + 273.15)

    print (fahr)
    print (kel)


"""
2. Calculadora de viagem
Crie uma função chamada calcular_combustivel() que receba a distância de uma viagem, 
o consumo do veículo em km/L e o preço do litro do combustível.
A função deve calcular e retornar a quantidade de litros necessária para a viagem 
e o custo total estimado.
Exemplo:
- Distância: 300 km
- Consumo: 10 km/L
- Preço do litro: R$ 6,00
- Resultado: 30 litros e R$ 180,00.

"""
def calcular_combustivel():

    distancia= float(input("Qual distancia:"))
    consumo= float(input("Qual consumo do veículo:"))
    preco= float(input("Preço por litro:"))

    totalconsu=distancia/consumo
    pre=preco*consu

    print(f"O consumo foi de {totalconsu}km")
    print(f"Preço do combustivel foi de {pre} R$")   




"""Crie uma função chamada calcular_troco() que receba o preço de um lanche 
e o valor pago pelo cliente.
A função deve retornar o troco. Caso o valor pago seja insuficiente, 
deve informar quanto falta para completar o pagamento.
Exemplo:
- Preço do lanche: R$ 18,50
- Valor pago: R$ 20,00
- Resultado: R$ 1,50 de troco.
"""
def calcular_troco():

   preco= float(input("Qual foi o preço de fabricação:"))
   pago= float(input("Valor pago pelo cliente:"))

   troco=preco-pago
   
   
   
   if preco < pago
   
   print (f"O valor foi insuficiente faltara {troco}")

   elif preco > pago

   print (f"{troco}")

calcular_troco()
