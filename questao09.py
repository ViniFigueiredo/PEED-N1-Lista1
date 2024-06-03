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
    menor = min(lista, key=lambda x: float(x) if isinstance(x, str) else x)
    #esta função anônima servirá para
    print("O menor número digitado foi:", menor)
else:
    print("Nenhum número foi digitado.")
