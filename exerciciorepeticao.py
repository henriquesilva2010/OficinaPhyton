"""
Exercícios — Laços de repetição em Python
1. Contagem regressiva — while
Faça um programa que mostre uma contagem regressiva de 10 até 1. Ao final, exiba a mensagem "Fim!".


2. Senha correta — while
Faça um programa que peça ao usuário para digitar uma senha.
Enquanto a senha estiver incorreta, peça para digitar novamente. Quando acertar, exiba "Acesso permitido!".
Considere a senha correta como 01234.

3. Tabuada — for e range()
Peça ao usuário um número inteiro e mostre a tabuada desse número, de 1 a 10.


4. Números pares — for e range()
Faça um programa que mostre todos os números pares de 0 até 20, utilizando for e range().


5. Soma dos números — for e range()
Peça ao usuário um número inteiro positivo.
Calcule e mostre a soma de todos os números de 1 até o número informado.
Exemplo: se o usuário digitar 5, o resultado será 15 (1 + 2 + 3 + 4 + 5).


6. Desafio — while e validação
Faça um programa que peça números inteiros ao usuário. 
O programa deve continuar recebendo números até que o usuário digite 0. 
Ao final, mostre a soma de todos os números digitados, sem contar o zero."""

contador = 10                                
while contador > 0:
    print(contador)
    contador = contador - 1


print(f"Fim") 

"""2. Senha correta — while
Faça um programa que peça ao usuário para digitar uma senha.
Enquanto a senha estiver incorreta, peça para digitar novamente. Quando acertar, exiba "Acesso permitido!".
Considere a senha correta como 01234."""

senha = "01234"
resul =input("Insira a senha:")

while resul != senha:
    print(f"Senha incorreta")
    resul =input("Insira a senha:")
print(f"Acesso permitido!")

"""3. Tabuada — for e range()
Peça ao usuário um número inteiro e mostre a tabuada desse número, de 1 a 10."""

nume =int(input(f"Insira um numero inteiro:"))
for i in range (1,11):
    print (f"{nume}x{i}={nume*i}")


"""4. Números pares — for e range()
Faça um programa que mostre todos os números pares de 0 até 20, utilizando for e range()."""

for i in range (2,21,2):
    print(i)

