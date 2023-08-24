# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# O t á v i o
# -6-5-4-3-2-1

#no python temos indices negativos também

nome = "Otávio"
print(nome[2]) # retorna á
print(nome[-4]) # retorna á

print(10 * '-')


print('a' in nome) # retorna True
print('z' in nome) # retorna False

print(10 * '-')

#IN verifica se está
print('Ot' in nome) # retorna True

#NOT IN verifica se não está
print('os' not in nome) # retorna True

print(10 * '-')

nome = input('Digite seu nome: ') 
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome :
    print(f'{encontrar} está em {nome}')
else :
    print(f'{encontrar} não está em {nome}')

#se digitar algum caractere que esteja no nome que foi passado pelo usuário vai retornar o If caso contrario Else