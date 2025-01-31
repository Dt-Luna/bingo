import random
modo_de_jogo = int(input('Indique o modo de jogo\n0 - RÁPIDO\n 1 - DEMORADO \n'))
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
                li.append([numeros_possiveis[n], False])
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

def status_de_sorteio(cartelas):
    for c in enumerate(cartelas):
        incompleto = False
        for l in c[1]:
            for e in l:
                if not e[0] in numeros_sorteados:
                    incompleto = True
        if incompleto == False:
            return [True, c[0]]
    return [False]
    
def jogadores(cartela):
    for coluna in enumerate(cartela):
        print(f'Jogador: {coluna[0] + 1}')
        for linha in coluna[1]:
            for i in range(len(linha)):
                numero, marcado = linha[i]
                if numero in numeros_sorteados:
                    linha[i][1] = True  
                
        for linha in zip(*coluna[1]): 
            linha_formatada = " | ".join(
                f' {num:2} ' if not marcado else f'({num:2})' for num, marcado in linha
            )
            print(linha_formatada)
        print('-' * 30)
                
def exibir(sorteado):
    print(f'\nÚltima dezena sorteada: {sorteado}')
    print(f'Dezenas sorteadas até o momento: {numeros_sorteados}\n')

def comecar_jogo():
    cartelas_do_jogo = gerar_cartela()
    exibir([])
    while True:
        sorteado=sortear_numero()
        exibir(sorteado)
        jogadores(cartelas_do_jogo)

               
        input('Pressione ENTER para continuar')

        situacao_de_vitoria = status_de_sorteio(cartelas_do_jogo)
        if situacao_de_vitoria[0]:
            print(f'Jogador {situacao_de_vitoria[1] + 1} é o ganhador =)')
            break

comecar_jogo()
