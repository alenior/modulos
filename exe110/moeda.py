def aumentar(preco=0, aumento=0, formata=False):
    aumentado = preco * (1 + (aumento / 100))
    return aumentado if formata is False else moeda(aumentado)


def diminuir(preco=0, diminuicao=0, formata=False):
    diminuido = preco * (1 - (diminuicao / 100))
    return diminuido if formata is False else moeda(diminuido)


def dobro(preco=0, formata=False):
    dobro = 2 * preco
    return dobro if not formata else moeda(dobro)


def triplo(preco=0, formata=False):
    triplo = 3 * preco
    return triplo if not formata else moeda(triplo)


def moeda(preco: float = 0, moeda='R$'):
    return f'{moeda} {preco:>.2f}'.replace(".", ",")


def resumo(preco, aumento, diminuicao):
    print(f'')
