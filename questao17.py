lista = []
while True:
    entrada = input("Digite um número ou 'sair' para encerrar: ")
    
    if entrada.lower() == 'sair':
    #função lower para identificar somente a palavra sair em lowercase
        break
    
    lista.append(entrada)
    try:
        numero = float(entrada)
        lista.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido ou 'sair' para encerrar.")

if lista:
    lista_numeros = [x for x in lista if isinstance(x, float)]
    lista_impares = [x for x in lista_numeros if x % 2 != 0]
    if lista_impares == []:
        print("Nenhum número ímpar foi digitado")
    else:    
        print("Soma dos números ímpares:", sum(lista_impares))
else:
    print("Nenhum número foi digitado.")
