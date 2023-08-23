# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que
# questiona se um valor é igual a outro
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))

#o interpretador ler da esquerda para a direita, de cima para baixo e resolve de dentro para fora
print(type(10 == 10))
print(type(10 == 11))

#Aqui ele retorna true e false pq o resultado da pergunta da uma valor booleano, então a tipagem se torna true ou false