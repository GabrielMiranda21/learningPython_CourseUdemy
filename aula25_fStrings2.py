"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC'
print(f'{variavel}')

#Se quisermos preencher com padding por algum motivo podemos preencher com espaços como argumento indicando dentro dos colchetes
#ao lado da variável com exemplo: *: >10*
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:$^11}')

#o sinal de + só indica para o python mostrar o sinal se for positivo ou negativo
print(f'{1000.4687453221354:0>+10,.1f}')

#hexadecimal
print(f'O hexadecimal de 1500 é {1500:08x}')

#conversion flags
print(f'{variavel!r}')
