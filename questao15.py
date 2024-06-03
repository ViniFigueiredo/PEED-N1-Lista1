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
    #list comprehension que armazena tudo depois do loop
    lista_menores_que_5 = [x for x in lista_numeros if x < 5]
    #list comprehension de todos os números maiores que 10
    if lista_menores_que_5 == []:
        print("Nenhum número que você digitou é menor que 5.")
    else:
        print("Números menores que 5:", lista_menores_que_5)
else:
    print("Nenhum número foi digitado.")