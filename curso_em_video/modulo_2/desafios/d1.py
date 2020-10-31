"""  
    Programa aprovar o emprestimo bancário
    Requisitos:
      -- interação com o usuário (perguntar o valor, em quantos anos irá pagar e o sálario do comprado)
      -- calcular o valor da parcela mensal
      -- as parcelas não podem esceder 30% do salário de quem pede o emprestimo (caso esceda ele não pode comprar)
    Resultado esperado:
"""

casaValor = float(input('Valor da casa: R$:'))
salario = float(input('digite seu salario: R$:'))
tempo = int(input('Tempo em que ira pagar o valor do emprestimo (em ano): '))

prestacao = 12 * tempo
minimo = (salario * 30) / 100

print('para pagar uma casa de R$:{:.2f} em {} anos'.format(casaValor, tempo, end=''))
print('a prestação será de {:.2f}'.format(prestacao))
if prestacao <= minimo:
  print('Emprestimo aprovado')
else:
  print('Emprestimo negado')
