def aumentar(preco=0, aumento=0, formatado=True):
    aumentado = preco * (1 + (aumento / 100))
    if formatado:
        print(f'Aumentando {aumento} %, o preço fica {moeda(aumentado)}.')
    else:
        print(f'Aumentando {aumento} %, o preço fica R$ {aumentado}.')


def diminuir(preco=0, diminuicao=0, formetado=True):
    diminuido = preco * (1 - (diminuicao / 100))
    if formetado:
        print(f'Diminuindo {diminuicao} %, o preço fica {moeda(diminuido)}.')
    else:
        print(f'Diminuindo {diminuicao} %, o preço fica R$ {diminuido}>')


def dobro(preco=0, formatado=True):
    dobro = 2 * preco
    if formatado:
        print(f'O dobro de {moeda(preco)} é {moeda(dobro)}.')
    else:
        print(f'O dobro de R$ {preco} é R$ {dobro}.')


def triplo(preco=0, formatado=True):
    triplo = 3 * preco
    if formatado:
        print(f'O triplo de {moeda(preco)} é {moeda(triplo)}.')
    else:
        print(f'O triplo de {preco} é {triplo}.')


def moeda(preco: float = 0, moeda='R$'):
    return f'{moeda} {preco:>.2f}'.replace(".", ",")
