
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

graus ()