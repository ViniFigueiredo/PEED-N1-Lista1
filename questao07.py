palavras = []

while True:
    entrada = input("Digite uma palavra ou '0' para encerrar: ")
    
    if entrada == '0':
        break
    
    palavras.append(entrada)

if palavras:
    maior_palavra = max(palavras, key=len)
    print("A maior palavra digitada foi:", maior_palavra)
else:
    print("Nenhuma palavra foi digitada.")
