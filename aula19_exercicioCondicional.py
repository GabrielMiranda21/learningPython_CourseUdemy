#input pede para o usuario digitar o valor e retorna sempre uma string/str

primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))

if primeiro_valor >= segundo_valor :
    print('O primeiro valor é maior ou igual ao segundo valor')
else :
    print('O segundo valor é maior do que o primeiro valor')

"""
    SOLUÇÃO:

    primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
"""