import random
#Trecho referente as funções criadas para este código
def Mov_Val (a,c,e):
    '''Função de validação para somas possíveis na estrutura do tabuleiro.
    a = Lista referente ao tabuleiro.
    c = O intervalo que deseja ser feito a leitura, sendo 4 para validação em linha e 16 para colunas.
    e = Lista que recebe a confirmação da possibilidade de soma.'''    
    
    e[0] = True
    b = 0
    cont = 0
    
    if c == 4 :
        d = 1
    elif c == 16 :
        d = 4
    
    for line in range(0, 4):
        if line > 0 and d == 1:
            b += 4
            c += 4
        if line > 0 and d == 4:
            b += 1
            c += 1
        for Cont in range (0,3) :
            for Contagem in range(b,c,d):
                if Contagem < (c-d) :
                    if a[Contagem] == a[Contagem+d] or a[Contagem] == 0 or a[Contagem + d] == 0 :
                        e[0] = False

def Soma_DE (a,c,e,f):
    """ Função destinada a movimentação, soma, confirmação de movimentação dos blocos e calculo de pontuação do 
    jogo
    a = indica qual listadeseja operar.
    c = O intervalo que deseja ser feito a soma, sendo 4 para linhas e 16 para colunas
    e = Lista que recebe a confirmação de soma ou movimentação do tabuleiro
    f = Lista que deve receber a somatória dos pontos"""    
    
    Validação = [[0], [0], [0], [0],
             [0], [0], [0], [0],
             [0], [0], [0], [0],
             [0], [0], [0], [0]]
    e[0] = False
    b = 0
    
    if c == 4:
        d = 1
    elif c == 16 :
        d = 4

    for line in range(0, 4):
        if line > 0 and d == 1:
            b += 4
            c += 4
        if line > 0 and d == 4:
            b += 1
            c += 1
        for Cont in range (0,3) :
            for Contagem in range(b,c,d):
                if Contagem < (c-d) :
                    if a[Contagem] == a[Contagem+d] and Validação[Contagem] != 1 and Validação[Contagem + d] != 1:
                        a[Contagem] = [a[Contagem][0] + a[Contagem+d][0]]
                        a[Contagem+d] = [0]
                        if (a[Contagem][0] + a[Contagem + d][0]) != 0 :
                            Validação[Contagem] = 1
                            f[0] = f[0] + a[Contagem][0]
                            e[0] = True

                            
                    if a[Contagem] == [0] and a[Contagem + d] != [0] :
                        a[Contagem] = [a[Contagem][0] + a[Contagem+d][0]]
                        a[Contagem+d] = [0]
                        e[0] = True

def Soma_ED (a,b,e,f): 
    """ Função destinada a movimentação, soma, confirmação de movimentação dos blocos e calculo de pontuação do 
    jogo
    a = indica qual listadeseja operar.
    b = O intervalo que deseja ser feito a soma, sendo 4 para linhas e 16 para colunas
    e = Lista que recebe a confirmação de soma ou movimentação do tabuleiro
    f = Lista que deve receber a somatória dos pontos"""    
    
    Validação = [[0], [0], [0], [0],
             [0], [0], [0], [0],
             [0], [0], [0], [0],
             [0], [0], [0], [0]]
    e[0] = False
    c = 0
    
    if b == 4:
        d = 1
    elif b == 16 :
        d = 4
    
    for line in range(0, 4):
        if line > 0 and d == 1:
            b += 4
            c += 4
        if line > 0 and d == 4 :
            b += 1
            c += 1
        for Cont in range (0,3) :
            for Contagem in range(b,c,-d):
                if Contagem < (b) :
                    if a[Contagem] == a[Contagem-d] and Validação[Contagem] != 1 and Validação[Contagem - d] != 1:
                        a[Contagem] = [a[Contagem][0] + a[Contagem-d][0]]
                        a[Contagem-d] = [0]
                        if (a[Contagem][0] + a[Contagem - d][0]) != 0 :
                            Validação[Contagem] = 1
                            f[0] = f[0] + a[Contagem][0]
                            e[0] = True
                            
                        
                    if a[Contagem] == [0] and a[Contagem - d] != [0] :
                        a[Contagem] = [a[Contagem][0] + a[Contagem-d][0]]
                        a[Contagem-d] = [0]
                        e[0] = True
                    
def Tabuleiro(tab):
     
     tab = [[0], [0], [0], [0],
             [0], [0], [0], [0],
             [0], [0], [0], [0],
             [0], [0], [0], [0]]
     return tab

# Atribuição de tipo a variáveis 
pontuacao = []
Movimentos = []
Jogo = True

# Laço de repetição referente ao reinício do jogo
while Jogo == True:

    tabuleiro = Tabuleiro('tab')
    Contagem_De_Movimentos = 0
    confirmacao = True
    Verificacao_De_Vitoria = False
    Verif_Derrota = False
    Conf = True
    Verificacao_De_Movimento = []
    Verificacao_De_Movimento.append(False) 
    Verif_Derrota_Vertical = [bool]
    Verif_Derrota_Vertical.insert(0,False)
    Verif_Derrota_Horizontal = [bool]
    Verif_Derrota_Horizontal.insert(0,False)
    Jogadas = 0
    Ponto = []
    Ponto.append(0)
#Laço de repetição para funcionamneto do jogo
    while confirmacao :

        Valida_Entrada = True
        Posicao_Disp = []
#Preencumento do tabuleiro:
    #Trecho referente a aquisição de espaços disponíveis no tabuleiro para receber os valores aleatórios
        for Contagem_De_0 in range(0,16):
            if tabuleiro[Contagem_De_0] == [0]:
                Posicao_Disp.append(Contagem_De_0)

    # Trecho referente a geração dos blocos aleátorios e contagem de movimentos caso haja um movimento válido
        Valor_Aleatorio = [2,4]
        if Verificacao_De_Movimento[0] == True :
            Contagem_De_Movimentos += 1

    #Trecho para geração de blocos aleatórios ao tabuleiro
            #Trecho para geração de dois blocos ao iniciar a partida
        if len(Posicao_Disp) == 16 :
            for c in range (0, 2):
                posição = random.choice(Posicao_Disp)
                tabuleiro[posição] = [random.choice(Valor_Aleatorio)]
            #Trecho para geração de um bloco aleatório caso seja possível.
        else: 
            if Verificacao_De_Movimento[0] == True and len(Posicao_Disp) > 0 :
                posição = random.choice(Posicao_Disp)
                tabuleiro[posição] = [random.choice(Valor_Aleatorio)]

#Trecho para validação de movimentos possívies caso todos os blocos do tabuleiro estejam preenchidos 
#Determinando assim se houve derrota do jogo
        if len(Posicao_Disp) == 1 :
            Mov_Val(tabuleiro,4,Verif_Derrota_Vertical)
            Mov_Val(tabuleiro,16,Verif_Derrota_Horizontal)

#Trecho para alidação da derrota 
        if Verif_Derrota_Vertical[0] == True and Verif_Derrota_Horizontal[0] == True :
            Verif_Derrota = True

#Trecho para validação de vitória
        for cont in range (0,16) :
            if tabuleiro[cont] == [2048] :
                Verificacao_De_Vitoria = True

#Trecho referente a apresentação do tabuleiro e botões de movimentos
        print()
        print()
        print(f'''|[{tabuleiro[0][0]:^4}] [{tabuleiro[1][0]:^4}] [{tabuleiro[2][0]:^4}] [{tabuleiro[3][0]:^4}]|
|[{tabuleiro[4][0]:^4}] [{tabuleiro[5][0]:^4}] [{tabuleiro[6][0]:^4}] [{tabuleiro[7][0]:^4}]|
|[{tabuleiro[8][0]:^4}] [{tabuleiro[9][0]:^4}] [{tabuleiro[10][0]:^4}] [{tabuleiro[11][0]:^4}]|
|[{tabuleiro[12][0]:^4}] [{tabuleiro[13][0]:^4}] [{tabuleiro[14][0]:^4}] [{tabuleiro[15][0]:^4}]|''')
        print()
        
        if  Verificacao_De_Vitoria == False and Verif_Derrota == False:
            print(f'Movimentos:{Contagem_De_Movimentos} Pontuação:{Ponto[0]}')
            print(f'''[A] ESQUERDA
[D] DIREITA
[W] CIMA
[S] BAIXO
''')

#Trecho referente a entrada e validação do usuário 

            while Valida_Entrada :
                try:
                    Entrada = str(input('Opção de movimento : ')).upper()
                    if Entrada == 'W' or Entrada == 'S' or Entrada == 'A' or Entrada == 'D' :
                        Valida_Entrada = False
                    else :
                        print('Digite uma opção válida')
                except :
                    print('COMANDO INVÁLIDO!!!')

#Trecho referente a quantidade de jogadas e movimentação baseada na informação de entrada           
        Jogadas += 1

        if Entrada == 'A' :
            Soma_DE(tabuleiro,4,Verificacao_De_Movimento,Ponto)
        if Entrada == 'D':
            Soma_ED(tabuleiro,4,Verificacao_De_Movimento,Ponto)
        if Entrada == 'W' :
            Soma_DE(tabuleiro,16,Verificacao_De_Movimento,Ponto)
        if Entrada == 'S' :
            Soma_ED(tabuleiro,16,Verificacao_De_Movimento,Ponto)

#Trecho referente a finalização do jogo
        if  Verificacao_De_Vitoria == True or Verif_Derrota == True:
            confirmacao = False
                
    print('')

#Trecho referente aos dados de finalização do jogo, além da opção de reiniciar o jogo
    Movimentos.append(Contagem_De_Movimentos)
    pontuacao.append(Ponto)
    print(f'''Histórico de movimentos: {Movimentos}''')
    print(f'Historico de pontuação: {pontuacao}')
    print('FIM DE JOGO')
    if Verificacao_De_Vitoria == True :
        print('VOCÊ VENCEU!!!')
    elif Verif_Derrota == True :
        print('VOCÊ PERDEU!!!')
    print()
    
    while Conf == True :
        try :
            Continuacao = str(input('Deseja reiniciar o jogo?[S/N] ')).upper()
            
            if Continuacao == 'S' :
                Conf = False
            elif Continuacao == 'N':
                Conf = False
            else :
                print('Resposta inválida!!!')
        except :
            print('COMANDO INVÁLIDO!')
            
    if Continuacao == 'N' :
        Jogo = False

#Trecho referente a mensagem de confirmação da finalização do código
print('Finalizando Jogo')
