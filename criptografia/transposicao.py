
texto = input("Digite o seu texto aqui: ")

lista_palavras = texto.split(" ")
nova_lista_palavras = []
quantidade_letras_transposicao = 2

for palavra in lista_palavras:
    tamanho_palavra = len(palavra)
    nova_palavra = ""

    if tamanho_palavra > quantidade_letras_transposicao:
        # bloco1 = palavra[0 : quantidade_letras_transposicao]
        # bloco2 = palavra[quantidade_letras_transposicao : ]
        # nova_palavra = bloco2 + bloco1
        bloco1 = palavra[-quantidade_letras_transposicao : ]
        bloco2 = palavra[0 : -quantidade_letras_transposicao]
        nova_palavra = bloco1 + bloco2
        nova_lista_palavras.append(nova_palavra)


print(' '.join(nova_lista_palavras))
