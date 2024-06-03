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
    produto = reduce(lambda x, y: x * y, lista_numeros)
    print("Produto de todos os números da lista:", produto)
else:
    print("Nenhum número foi digitado.")
