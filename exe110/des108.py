import moeda

preco = float(input('Qual o preço a ser modificado? R$ '))
aumento = float(input('Qual o aumento (%) a ser aplicado? '))
diminuicao = float(input('Qual a diminuição (%) a ser aplicada? '))

print(f'O preço aumentado fica {moeda.aumentar(preco, aumento, False)}.')
print(f'O preço diminuído fica {moeda.diminuir(preco, diminuicao, False)}.')
print(f'O preço dobrado fica {moeda.dobro(preco, False)}.')
print(f'O preço triplicado fica {moeda.triplo(preco, False)}.')
