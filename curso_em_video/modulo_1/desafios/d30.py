""" 
    Olha a multa
    80km é o limite
    7 reias a cada km acima de 80 
"""

""" 
    Requisistos:
    var inteiro = com um número já definido de 0 a 5
    interação com o usuário
    notíciar a vitória com msg na tela
"""
import emojis


limite_vel = 80
val_user = float(input('Digite a velocidade do veículo: '))

if  limite_vel <= val_user:
    valor = val_user % limite_vel
    multa = valor * 7
    print(
        emojis.encode("""  
        Limite de velocidade excedido :rotating_light:, você receberá uma multa de R$:{:.2f} 
    """).format(multa))
else:
    print(
        emojis.encode("""  
        Dentro da lei cidadão, vá sem presa, de vagar e sempre  :blue_car::car::oncoming_police_car:
    """))
    

