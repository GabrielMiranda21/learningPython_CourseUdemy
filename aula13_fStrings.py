nome = "Gabriel";
altura = 1.75;
peso = 90;
imc = peso / int(altura * altura); 

dinheiro = 10000

#Existem vários tipos de formatação de String mas umas dela é o F que quando colocado antes de uma String nos permite colocar váriaveis dentro da String
#para colocarmos uma váriavel dentro de uma string precisamos envolve-las por chaves como abaixo
exemplo_1 = f"O {nome} tem o peso de {peso}kilos e tem a altura de {altura}";
print(exemplo_1)

#podemos definir também quantas casas decimais queremos exibir em um valor float
exemplo_2 = f"O {nome} tem {altura:.3f} de altura"
print(exemplo_2)

#as vezes queremos exibir os valores de dinheiros com virgula para isso podemos fazer assim
exemplo_3 = f"{dinheiro:,.2f}"
print(exemplo_3)

#f-Strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)