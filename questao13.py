palavras = []

entrada = input('Digite uma lista de palavras separadas por espaço:')

palavras = entrada.split()

palavras_com_a = [palavra for palavra in palavras if palavra.lower().startswith('a')]

print(f'Palavras que começam com a: {palavras_com_a}')
        