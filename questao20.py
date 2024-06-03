from functools import reduce

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
    lista_numeros.sort(reverse=True)
    print("Lista de núemros ordenada:", lista_numeros)
else:
    print("Nenhum número foi digitado.")
