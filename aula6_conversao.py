# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo de dado em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool

"""
    Existem funções que ele só converte um tipo em outro se isso puder ser feito
"""


#Lembrando que ele sempre da prioridade aos parenteses de dentro, ele le de dentro para fora
print(int('1'), type(int('1')))
print(type(float('1') + 1))

#Quando convertemos uma string em um valor booleano e ela está vazia é False, uma string com qualquer valor é True
print(bool(' '))


print(str(11) + 'b')