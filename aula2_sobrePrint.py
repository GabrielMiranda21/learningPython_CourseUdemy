#por padrão a função print exibe os argumentos, e coloca espaços e quebra de textos

print(12, 34);
print(56, 78);

#posso definir outro separador também, é necessário apresentar como argumento *sep=''* e o simbolo que gostaria de usar para separar

print(1, 2, 3, sep="-")
print(1, 2, 3, sep="*")
print(1, 2, 3, sep="joao")

"""
    No canto inferior do windows direito a palavra CRLF é Creative return life feed que 
    é um tipo de quebra de texto espefico do windows representados por *\r\n* - return e linefeed
    Ele é um caractere que a gente não vê, mas que quebra a linha
    Dependendo do sistema operacional é usado outros tipos de quebra de texto espefico.
"""
#Outro argumento para o print é *end* que por padrão no windows é end="\r\n " mas se a gente utilizar somente *\n* ele também entende
print(1, 2, 3, end="\r\n")
print(1, 2, 3, end="*\n")
print(1, 2, 3, end="\n##")

# se alterarmos a ordem a quebra de linha não acontece

print(1, 2, 3, end="*")
print(1, 2, 3, end="\n")

#O python diferencia caracteres maiusculos de minisculos pois para ele caractere com letra maiuscula ou minusculas são outras coisas