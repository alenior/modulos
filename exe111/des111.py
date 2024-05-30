from utilidadesCeV import moeda
from utilidadesCeV import dado

preco = dado.leiaDinheiro(f'Informe o preço a ser analisado: R$ ')
aumento = float(input('Qual o aumento (%) a ser aplicado? '))
diminuicao = float(input('Qual a diminuição (%) a ser aplicada? '))

moeda.resumo(preco, aumento, diminuicao)
