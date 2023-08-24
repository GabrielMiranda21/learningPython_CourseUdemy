# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado verdadeira,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0, 0.0, '', False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else : 
    print('Sair')

#avaliação de curto circuito
#OR qualquer valor que seja avaliado como True irá passar adiante
print(True and False and True)