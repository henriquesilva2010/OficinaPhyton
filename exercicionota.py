"""Peça o nome do aluno e logo em seguida receba 3 ou mais notas, calcule a média e informe a situação do aluno:

Se media for menor que 5 aluno está reprovado
Se for de 5 e menor que 7 está em recuperação
igual maior que 7 aluno está aprovado"""

nomedoaluno=str(input("Nome do aluno:"))
nota1=float(input("Nota da Prova:"))
nota2=float(input("Nota de comportamento:"))
nota3=float(input("Nota do exercicio:"))

media=(nota1 + nota2 + nota3) /3

if media<5:
    print(f"Aluno não alcançou a nota esperada")
elif media>=5 and media<=6:
    print(f"O aluno ficou de recuperação")
elif media>7:
    print(f"O aluno atingiu a nota esperada para passar de ano")