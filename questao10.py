lista = []
while True:
    entrada = input("Digite um número ou 'sair' para encerrar: ")
    
    if entrada.lower() == 'sair':
        break
    
    lista.append(entrada)
    try:
        numero = float(entrada)
        lista.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido ou 'sair' para encerrar.")

if lista:
    numeros = [x for x in lista if isinstance(x, float)]
    #list comprehension 
    soma = sum(numeros)
    media = soma / len(numeros)
    print("A média dos números digitados foi:", media)
else:
    print("Nenhum número foi digitado.")
