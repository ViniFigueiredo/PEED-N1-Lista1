numeros = []
while True:
    entrada = input("Digite um número ou 'exit' para encerrar: ")
    
    if entrada.lower() == 'exit':
        break
    
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido ou 'exit' para encerrar.")

print("Os números na lista são:", numeros)

soma = sum(numeros)
print("A soma dos números na lista é:", soma)
