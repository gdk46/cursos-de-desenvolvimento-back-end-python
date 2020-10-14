diaria = 60
carro_km = 0.15

dias_aluguel = float(input('Quantos dias de aluguel? '))
km_rodados = float(input('Quantos quilometros foram rodados? '))

preco_total = (dias_aluguel * diaria) + (carro_km * km_rodados)

print('preco total do aluguel R$: {:.2f}'.format(preco_total))