n = 5
linha = 1

while linha <= n:
    coluna = 1
    while coluna <= (n - linha + 1):
        print(coluna, end=' ')
        coluna += 1
    print()  # pula para a próxima linha
    linha += 1