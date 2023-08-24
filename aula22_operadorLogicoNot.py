# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')

print(not True)  # False
print(not False)  # True

senha = input('Senha: ')

"""
if senha == '123456' :
    print('Entrou')
else:
    print('Senha incorreta')

Da para fazer assim porém tem jeitos melhores

if senha != '123456' :
    print('Senha incorreta')
exemplo: Pode ser que a senha incorreta seja checada primeiro
"""

#String vazia é false
#nesse caso se o usuario não digitar nada o if vai avaliar como true e vai exibir Você não digitou nada

if not senha :
    print('Você não digitou nada')

#basicamente o operador not ele inverte a expressão 