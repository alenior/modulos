def aumentar(preco=0, aumento=0):
    aumentado = preco * (1 + (aumento / 100))
    print(f'Aumentando {aumento} %, o preço fica R$ {moeda(aumentado)}.')


def diminuir(preco=0, diminuicao=0):
    diminuido = preco * (1 - (diminuicao / 100))
    print(f'Diminuindo {diminuicao} %, o preço fica R$ {moeda(diminuido)}.')


def dobro(preco=0):
    dobro = 2 * preco
    print(f'O dobro de R$ {moeda(preco)} é R$ {moeda(dobro)}.')


def triplo(preco=0):
    triplo = 3 * preco
    print(f'O triplo de R$ {moeda(preco)} é R$ {moeda(triplo)}.')


def moeda(preco: float = 0, moeda='R$'):
    return f'{moeda} {preco:>.2f}'.replace(".", ",")
