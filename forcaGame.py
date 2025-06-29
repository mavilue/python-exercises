secreto = 'dinossauro'
lista = []

while True:
    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("Isso não é válido, tente novamente!")
        continue

    lista.append(letra)

    if letra in secreto:
        print(f"A letra {letra} está na palavra secreta!")
    else:
        print(f"A letra {letra} não está na palavra secreta!")
        lista.pop()

    digitados = ''
    for letra_secreta in secreto:
        if letra_secreta in lista:
            digitados += letra_secreta
        else:
            digitados += '*'
    print(digitados)

    if digitados == secreto:
        print()
        print("Parabéns, você descobriu a palavra secreta.")
        break
