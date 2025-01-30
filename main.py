import random

modo_de_jogo = int(input())
numero_maximo = 0
if modo_de_jogo == 1:
    numero_maximo = 40
elif modo_de_jogo == 0:
    numero_maximo = 30
numeros_sorteados = []
numeros_possiveis = [n for n in range(1, numero_maximo + 1)]

def gerar_cartela():
    if modo_de_jogo == 1:
        ncartelas = 4
        ncolunas = 4
        nlinhas = 3
    elif modo_de_jogo == 0:
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

def sortear_numero():
    sorteado = random.choice(numeros_possiveis)
    numeros_sorteados.append(sorteado)
    numeros_possiveis.remove(sorteado)
    return(sorteado)

def comecar_jogo():
    


    print(gerar_cartela())

    i=0
    while i < 30:
        print(sortear_numero())
        i+=1

comecar_jogo()