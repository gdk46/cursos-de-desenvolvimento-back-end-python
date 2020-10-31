"""  
    Programa aprovar o emprestimo bancário
    Requisitos:
      -- interação com o usuário (perguntar o valor, em quantos anos irá pagar e o sálario do comprado)
      -- calcular o valor da parcela mensal
      -- as parcelas não podem esceder 30% do salário de quem pede o emprestimo (caso esceda ele não pode comprar)
    Resultado esperado:
"""

# casaValor = float(input('Valor da casa: R$'))
# salario = float(input('digite seu salario'))
# tempo = int(input('Tempo em que ira pagar o valor do emprestimo (em ano)'))
casaValor = 10000
salario = 1.000
tempo = 40

quantidadeMes = 12 * tempo
casaPorcentagem = (casaValor * 30) / 100
porcentagemParcela = ""
porcetagem = ""

print(casaPorcentagem)
