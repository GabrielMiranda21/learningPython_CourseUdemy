# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0, 0.0, '', False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

#O if só será executado se a expressão toda for true
#se a primeira expressão for avaliada como false, ele não lê a segunda
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else : 
    print('Sair')

#Quando os valores 0 0.0 '' são confrontados com booleanos dão valores falso
print(bool(''))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(False))
      

#avaliação de curto circuito
#AND qualquer valor que seja avaliado como False invalidará toda a expressão
print(True and False and True)