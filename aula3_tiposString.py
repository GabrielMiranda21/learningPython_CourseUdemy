#Python é uma linguagem de porgramação com TIPAGEM DINÂMICA forte, que pode variar de linguagem sendo fraca, forte, dinamica e estatica
#O python combina essa duas caracteristicas que combina ser Dinamica e Forte. Isso significa que o python sabe o dado que você está passando 


#tipos de dados

#numero inteiro
print(1234);

#string
print('aspas simples')
print("aspas duplas")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#escape
"""
    -representado por *\* serve para dizer quando não queremos que algum caracter seja interpretado
    -A diferença é o caracter que não foi interpetrado passa a fazer parte da string
"""
print("olá \"Gabriel")

#r
"""
    Agora se quisermos que as barras apareçam juntos só precisamos indicar antes com *r* que ele entende
"""
print(r"Olá \"Gabriel\"")


#para ficar clean code podemos fazer dessa forma também
print(1, 'olá "Gabriel"')
#se invertermos também funciona
print(2, "olá 'Gabriel'")