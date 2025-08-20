lista = []

while True:
    print('\nSelecione uma opção:')
    escolha = input('[i]inserir [a]apagar [l]listar [s]sair: ').lower().strip()

    if escolha not in ('i', 'a', 'l', 's'):
        print('Por favor, escolha apenas i, a, l ou s!')
        continue

    if escolha == 'i':
        valor = input('Valor: ')
        lista.append(valor)

    elif escolha == 'l':
        if len(lista) == 0:
            print('Lista vazia.')
        else:
            for indice, item in enumerate(lista):
                print(indice, item)

    elif escolha == 'a':
        try:
            deletar = int(input('Escolha o índice para apagar: '))
            del lista[deletar]
            print('Item removido!')
        except ValueError:
            print('Digite um número válido.')
        except IndexError:
            print('Índice inexistente na lista.')

    elif escolha == 's':
        print('Até a próxima!')
        break