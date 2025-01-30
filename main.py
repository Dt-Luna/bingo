import random
def gerar_cartela(m):
    if m == 1:
        ncartelas = 4
        ncolunas = 4
        nlinhas = 3
    elif m == 0:
        ncartelas = 2
        ncolunas = 3
        nlinhas = 2

    cartelas = []
    for _ in range(ncartelas):
        a, b = 1, 11
        cartela = []
        for _ in range(0,ncolunas):
            li = []
            numeros_possiveis = [n for n in range(a, b)]
            for _ in range(0,nlinhas):
                n = random.randint(0, len(numeros_possiveis) - 1)
                li.append(numeros_possiveis[n])
                numeros_possiveis.pop(n)
            a += 10
            b += 10
            cartela.append(li)
        cartelas.append(cartela)
    return cartelas

print(gerar_cartela(1))

        

