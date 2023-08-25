"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

"""
nome = input('Digite seu primeiro nome: ')
idade = input('Digite sua idade: ')
contenEspacos = nome not in '' 

if nome == nome and idade == idade : #Aqui o valor que usuario digitou vai sempre dar true porque a pergunta é 'nome tem o mesmo valor que o nome'
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome contém {str(contenEspacos)}') #podemos fazer if dentro de if
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else :
    print('Desculpe, você deixou campos vazios')
"""



#SOLUÇÃO
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")