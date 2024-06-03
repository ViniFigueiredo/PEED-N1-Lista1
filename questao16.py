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
    lista_pares = [x for x in lista_numeros if x % 2 == 0]
    if lista_pares == []:
        print("Nenhum número par foi digitado")
    else:    
        print("Soma dos números pares:", sum(lista_pares))
else:
    print("Nenhum número foi digitado.")
