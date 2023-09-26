
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

soma = n1 + n2

media = soma/2 

if media < 7:
    print("Reprovado")
elif media < 10:
    print("Aprovado")
else:
    print("Aprovado com distinção")

print("Media: ", media)