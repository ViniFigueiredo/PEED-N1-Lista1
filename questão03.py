from math import sqrt

num = float(input("Digite um número positivo: "))

while True:
    if num >= 0:
        break
    else:
        num = float(input("Digite um número positivo: "))

raiz = sqrt(num)
print("A raiz quadrada de", num, "é igual a:", raiz)
