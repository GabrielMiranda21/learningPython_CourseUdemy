"""
    Interpolação básica de strings
    s - string
    d e i - int
    f - float
    x e X - Hexadecimal(ABCDEF0123456789)
"""

#interpolação é o mesmo que format só que de um jeito diferente

#Para usarmos a interpolação devemos indicar o tipo através da expressão %tipo e depois fora da String %(as variavéis na ordem de execução)

nome = 'Gabriel'
preco = 1000.95897643
variavel = '%s, o preco é R$%.2f' % (nome, preco)
print(variavel)

"""
    Para calcular os hexadecimal usamos o x minusculo para gerar um hexadecimal minusculo e X maiusculo para gerar um hexadecimal maiusculo
"""

print('O hexadecimal de %d é %x' % (15, 15))

#se a gente quiser preencher o hexadecimal com 0 podemos colocar antes do x a quantidade de zeros
print('O hexadecimal de %d é %04x' % (15, 15))
