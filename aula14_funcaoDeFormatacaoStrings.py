#format é método nativo do python, ele recebe argumentos 
a = "A"
b = "B"
c = 1.1

formato = "a={} b={} c={}".format(a, b, c)
print(formato)



#pode ser feito de outra forma também
#conseguimos também formatar em f-String

d = "D"
e = "E"
f = 1.2

#se colocarmos um quarto argumento sendo que passamos apenas 3 daria erro
#Podemos pegar valores por indices também, assim não depedendo da ordem

exemplo1 = "d={} e={} f={:.3f}" 

formato2 = exemplo1.format(d, e, f)

print(formato2)

#parametro nomeado é quando eu dou um nome para as coisas dentro da chamada das funções
#ou das criações da funções
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

#a partir do momento que eu nomeio um argumento com um parametro, tudo que vier depois precisa ser nomeado já o que estiver antes não é necessário
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
