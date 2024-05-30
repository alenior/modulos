import moeda

preco = float(input('Qual o preço a ser modificado? R$ '))
aumento = float(input('Qual o aumento (%) a ser aplicado? '))
diminuicao = float(input('Qual a diminuição (%) a ser aplicada? '))

moeda.resumo(preco, aumento, diminuicao)
