import nltk


# Abrindo o arquivo


with open("dados/artigos.txt", "r", encoding='UTF-8') as f:
    artigos = f.read()


# Tokenizando com NLTK


lista_tokens = nltk.tokenize.word_tokenize(artigos)


# Funcao para separar as palavras


def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)
    return lista_palavras


# Funcao para normalizar


def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada


lista_palavras = separa_palavras(lista_tokens)
lista_normalizada = normalizacao(lista_palavras)
set(lista_normalizada)