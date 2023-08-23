"""
    Nivel de precedencia/Herarquia

    1. (n + n)
    2. **
    3. * / // %
    4. + -


"""

# 

##predencia de operadores significa que algumas coisas serão executas primeiro
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5) #na exponenciação o valor da esquerda é o valor inteiro e a direita é o elevado/exponente
print(conta_1)