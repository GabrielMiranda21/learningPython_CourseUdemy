"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

#omitir - passar nenhum resultado, o python entende que é pra ir do inicio ou até o fim dependendo do indice
variavel = 'Olá mundo'

#Fatiamento [i:f:p]
print(variavel[0:len(variavel):1])
print(variavel[::-1])
print(variavel[-1:-10:-1])

#primeiro parametro indice:indice
#trás o resultado a partir do indice 4
print(variavel[4:])

#inicio e fim
print(variavel[4:8])

#inicio e fim com negativos
#indices negátivos conta de trás para frente e positivo o contrário
print(variavel[-8:-2])

#função len
print(len(variavel))
print(len(variavel[::-1]))