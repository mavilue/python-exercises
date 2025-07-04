while True:
    cpf = input("Digite seu CPF: ")

    if (len(cpf)!=11) or not (cpf.isnumeric()):
        print("CPF INVÁLIDO! TENTE NOVAMENTE.")
        continue

    else:
        '''CALCULANDO O PRIMEIRO DÍGITO'''
        print("=" * 15)
        print("PRIMEIRO DIGITO ")
        print("=" * 15)

        # Multiplicando cada número por seu peso
        vet_cpf: [int] = [int(cpf[i]) for i in range(9)]    # 'cpf[i]' é cada caractere e 'int' é p/ passar de str p/ num
        soma1=0
        for i in range(9):
            peso = 10-i #regra de peso do cpf
            priMultip = peso*vet_cpf[i]
            soma1 += priMultip
            print(f'{vet_cpf[i]} x {peso} = {priMultip}')
        print("--"*10)
        print(f"SOMA TOTAL = {soma1}")

    # Obtendo o primeiro dígito após a soma
    divis1 = soma1 % 11

    if not divis1<=1:
        digito1 = 11 - divis1
        print(f"Primeiro dígito = {digito1}")

    else:
        digito1 = 0
        print(f"Primeiro dígito = {digito1}")


    '''CALCULANDO O SEGUNDO DÍGITO'''
    print()
    print("="*15)
    print("SEGUNDO DIGITO ")
    print("="*15)

    # Multiplicando cada número por seu peso após obter o primeiro dígito
    soma2 = 0
    for i in range(9):
        peso2 = 11-i
        segMultip = peso2 * vet_cpf[i]
        soma2 += segMultip
        print(f'{vet_cpf[i]} x {peso2} = {segMultip}')

    # incluindo o primeiro dígito
    terMulti = digito1 * 2
    print(f'{digito1} x 2 = {terMulti}')
    soma2 += terMulti
    print("--"*10)
    print(f"SOMA TOTAL = {soma2}")

    # Obtendo o segundo dígito após a soma
    divis2 = soma2 % 11

    if not divis2<=1:
        subt2 = 11 - divis2
        print(f"Segundo dígito = {subt2}")

    else:
        subt2 = 0
        print(f"Segundo dígito = {subt2}")

    break