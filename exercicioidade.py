"""
Crie um programa que solicite o nome e a idade de uma pessoa.
 Depois, classifique-a como Criança, Adolescente ou Adulto,
de acordo com a idade, e exiba todas as informações
de forma organizada."""

nome=(input("Seu nome:"))
ida=int(input("Sua idade:"))

if ida <= 12:
    print(f"Você é uma criança não podera acesar pela sua idade")
elif ida>12 and ida>=17:
    print(f"Você é uma adolecente tera restrições pela sua idade")
elif ida>=18:
    print(f"Você é um adulto aceso permitido pela sua idade")


print 
print
print
print

contador = 0
while contador < 3:
    contador = contador + 1
    print(f"Resultado {contador}")

for i in range(3):
    print(f"Print {i+1}")

for i in range(12,17):
    print(f"Print {i}")


for i in range(14,517,20):
    print(f"Print {i}")


