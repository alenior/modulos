def aumentar(preco, aumento):
    aumentado = preco * (1 + (aumento / 100))
    print(f'Aumentando {aumento:.2f} %, o preço fica R$ {aumentado:.2f}.')


def diminuir(preco, diminuicao):
    diminuido = preco * (1 - (diminuicao / 100))
    print(f'Diminuindo {diminuicao:.2f} %, o preço fica R$ {diminuido:.2f}.')


def dobro(preco):
    dobro = 2 * preco
    print(f'O dobro de R$ {preco:.2f} é R$ {dobro:.2f}.')


def triplo(preco):
    triplo = 3 * preco
    print(f'O triplo de R$ {preco:.2f} é R$ {triplo:.2f}.')
