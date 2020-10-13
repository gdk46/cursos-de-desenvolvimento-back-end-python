#calcular preco de um produto
#o produto deve ter 5% de desconto  
preco = float(input('digite o preço do profuto: '))
desconto = float(input('digite a porcentagem em desconto que deseja dá: '))
desconto_t = 100 - desconto
a = (preco * desconto_t) / 100
print('o preço com o desconto fica R$: {:.0f}'.format(a))