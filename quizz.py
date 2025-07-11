questoes = {
    'PERGUNTA 01': {
        'pergunta': 'Qual é o planeta mais próximo do Sol?', #texto da pergunta
        # outro dicionario com as alternativas:
        'resposta': {
            'a': 'Terra',
            'b': 'Mercúrio',
            'c': 'Vênus',
        },
        'resposta_certa': 'b',
    },
    'PERGUNTA 02': {
        'pergunta': 'Qual é o principal gás responsável pela respiração humana?',  # texto da pergunta
        # outro dicionario com as alternativas:
        'resposta': {
            'a': 'Oxigênio',
            'b': 'Gás Carbônico',
            'c': 'Nitrogênio',
        },
        'resposta_certa': 'a',
    },
    'PERGUNTA 03': {
        'pergunta': ' Qual é o estado físico da água em temperatura ambiente?',
            'resposta': {
            'a': 'Sólido',
            'b': 'Líquido',
            'c': 'Gasoso',
        },
        'resposta_certa': 'b',
    },
}

resposta_certa=0
#perguntas exibidas pk-pergunta 1, pergunta 2; pc-detalhes da pergunta 'texto da perg'
for pk, pc in questoes.items():
    print(f'{pk}: {pc["pergunta"]}')

# rk-alternativa ; rc- detalhe da alternativa 'no caso o texto'
    print('Resposta: ')
    for rk, rc in pc["resposta"].items():
        print(f'{rk}: {rc}')

    resposta_usuario = input("Digite sua resposta: ")
    if resposta_usuario == pc['resposta_certa']:
        print('RESPOSTA CERTA!')
        resposta_certa += 1
    else:
        print('RESPOSTA ERRADA!')
    print()

print(f'Quantidade total de acertos: {resposta_certa}')
