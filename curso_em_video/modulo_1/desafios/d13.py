#calcular preco de um produto
#o produto deve ter 5% de desconto  
preco = float(input('qual o salario do funcionário R$: '))
acresimo = float(input('digite a porcentagem de acresimo que deseja dá: '))
a = preco + (preco * acresimo  / 100)
print('o preço com o desconto fica R$: {}'.format(a))