"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

#para códigos que nunca vai mudar usa-se letras maiusculas por boas praticas
#códigos com varias blocos de códigos tornam ele complexo


"""
velocidade = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if RADAR_1 < velocidade :
    print('você ultrapassou o limite')
"""

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')

#código clean code/código limpo