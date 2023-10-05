n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo: "))
n3 = float(input("Digite o terceiro: "))

maior = n2

if maior < n1:
    maior = n1
if maior < n3:
    maior = n3
print("O maior é: ",maior)

menor = n2

if menor > n1:
    menor = n1
if menor > n3:
    menor = n3
print ("O menor é: ",menor)