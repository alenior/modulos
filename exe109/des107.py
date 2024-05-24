import moeda

preco = float(input('Qual o preço a ser modificado? R$ '))
aumento = float(input('Qual o aumento (%) a ser aplicado? '))
diminuicao = float(input('Qual a diminuição (%) a ser aplicada? '))
formatado = bool(input('Exibir com formatação? '))

moeda.aumentar(preco, aumento, formatado)
moeda.diminuir(preco, diminuicao, formatado)
moeda.dobro(preco, formatado)
moeda.triplo(preco, formatado)
help(bool)
