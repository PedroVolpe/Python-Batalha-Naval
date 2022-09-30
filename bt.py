#------------------------------------------------------------------------------------------------------------------------

#Informações do aluno

#Pedro Loureiro Morone Branco Volpe           TIA:42131936
#Turma: 02D 

#------------------------------------------------------------------------------------------------------------------------

import random

#------------------------------------------------------------------------------------------------------------------------

def criaMatriz(M,tam):
    for i in range(tam+1):
        linha = []
        for j in range(tam+1):
            linha.append(' .')
        M.append(linha)
    
    tab = []
    for k in range(len(M)):
        linhat = []
        if k == 0:
            linhat.append(' ')
            for l in range(1,len(M)):
                linhat.append(' '+str(l))
        else:
            linhat.append(str(k))
            for m in range(len(M)):
                linhat.append(M[k][m])
        tab.append(linhat)

    return tab
#------------------------------------------------------------------------------------------------------------------------
def posicionaEmbarcacoes(M, E, linha, coluna, posi, letra):#tabuleiro, 2/3/4/5, linha, coluna, H/V, S/C/E/P   
    verifica = 0
    if posi == 1:        
        if coluna <= (len(M[0])-E):            
            cont=coluna
            for j in range(E): #verifica se os espaços estão liberados          
                if M[linha][cont] == ' .':                    
                    verifica+=1                
                cont+=1
            cont=coluna        
            if verifica == E: #se todos os espaços estiverem liberados, então posiciona embarcação
                for j in range(E):                    
                    M[linha][cont] = letra                    
                    cont+=1
                return M, True
    else:           
        if  linha <= (len(M)-E):            
            cont = linha
            for x in range(E): #verifica se os espaços estão liberados                
                if M[cont][coluna] == ' .':                    
                    verifica+=1                
                cont+=1
            cont=linha
            if verifica == E: #se todos os espaços estiverem liberados, então posiciona embarcação               
                for i in range(E):                        
                    M[cont][coluna] = letra                
                    cont+=1
                return M, True
    return M, False
#------------------------------------------------------------------------------------------------------------------------
def atira(M,linha,coluna):

    if (M[linha][coluna] == ' S') or (M[linha][coluna] == ' C') or (M[linha][coluna] == ' E') or (M[linha][coluna] == ' P'):
        acerto = M[linha][coluna]
        M[linha][coluna] = ' X'
    elif M[linha][coluna] == ' .':
        acerto = M[linha][coluna]
        M[linha][coluna] = ' O'
    elif (M[linha][coluna] == ' X') or (M[linha][coluna] == ' O'):
        acerto = M[linha][coluna]

    return M,acerto
#------------------------------------------------------------------------------------------------------------------------
def imprime(M,tipo):
    print(f'Tabuleiro do {tipo}')
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j],end=' ')
        print( )
#------------------------------------------------------------------------------------------------------------------------
def main():

    M = []
    Mbot = []
    tam = 10
    M = criaMatriz(M,tam)
    Mbot = criaMatriz(Mbot,tam)
    bot = 'bot'
    jog = 'jogador'  

    #------------------------------------------------------------------------------------------------------------------------

    #GERANDO O TABULEIRO DO ADVERSÁRIO (BOT)

    contb = 2 
    while contb<=5:

        if contb == 2:
            letrab = ' S'            
        elif contb == 3:
            letrab = ' C'
        elif contb == 4:
            letrab = ' E'
        else:
            letrab = ' P'

        linhab = random.randint(1,10)
        colunab = random.randint(1,10)
        posib = random.randint(0,1)

        Mbot,flagb = posicionaEmbarcacoes(Mbot,contb,linhab,colunab,posib,letrab)

        if flagb == True:
            contb+=1

    #------------------------------------------------------------------------------------------------------------------------

    #BLOCO DO JOGADOR 

    imprime(M,jog) 

    cont=2
    while cont<=5:

        if cont == 2:
            letra = ' S'            
        elif cont == 3:
            letra = ' C'
        elif cont == 4:
            letra = ' E'
        else:
            letra = ' P'

        linha = int(input(f'DIGITE A LINHA QUE DESEJA POSICIONAR  O/A {letra}: '))
        coluna = int(input(f'DIGITE A COLUNA QUE DESEJA POSICIONAR  O/A {letra}: '))
        posi = int(input(f'DIGITE 1 PARA HORIZONTAL E 0 PARA VERTICAL, PARA POSICIONAR  O/A {letra}: '))

        M,flag = posicionaEmbarcacoes(M,cont,linha,coluna,posi,letra)

        if flag == True:
            imprime(M,jog)
            cont+=1
        else:
            print("REPOSICIONANDO...................................")
    
    #------------------------------------------------------------------------------------------------------------------------

    

    turno = True
    tiros = 0
    tirosb = 0

    p,e,c,s = True,True,True,True
    pb,eb,cb,sb = True,True,True,True

    while turno == True:
        
        lista_acertos = []
        while tiros <= 20 and turno == True:

                imprime(M,jog)

                tlinha = int(input(f'\nRODADA {tiros}, DIGITE A LINHA QUE DESEJA ATACAR: '))
                tcoluna = int(input(f'RODADA {tiros},DIGITE A COLUNA QUE DESEJA ATACAR: '))
                Mbot,acerto = atira(Mbot,tlinha,tcoluna)

                if (acerto == ' X') or (acerto == ' O'):
                    print('\nJa atacou essa posição, tente novamente na proxima rodada') 
                elif acerto == ' .':
                    print('\nAcertou a agua')
                    tiros += 1
                elif (acerto == ' S') or (acerto == ' C') or (acerto == ' E') or (acerto == ' P'):
                    lista_acertos.append(acerto)
                    print(f'\nAcertou a embarcação: {acerto}')
                    tiros += 1

                for v in range(len(lista_acertos)):
                
                    if lista_acertos[v] == ' P':
                       
                       p = False
                    elif lista_acertos[v] == ' E':
                       
                       e = False
                    elif lista_acertos[v] == ' C':
                       
                       c = False
                    elif lista_acertos[v] == ' S':
                       
                       s = False

                    if p == False and e == False and c == False and s == False:
                        tiros = 21
                        print('\nCAMPO DO BOT')
                        imprime(Mbot,bot)
                        print('Voce venceu.\nAcertou todas as embarcações inimigas!!')
                        break

                turno = False
        
        lista_acertosb = []
        while tirosb <= 20 and turno == False:

                imprime(Mbot,bot)

                tlinha = random.randint(1,10)
                tcoluna = random.randint(1,10)
                M,acertob = atira(M,tlinha,tcoluna)
                if (acertob == ' X') or (acertob == ' O'):
                    pass

                elif acertob == ' .':
                    tirosb += 1

                elif (acertob == ' S') or (acertob == ' C') or (acertob == ' E') or (acertob == ' P'):
                    lista_acertosb.append(acertob)
                    tirosb += 1
            
                for vb in range(len(lista_acertosb)):
                
                    if lista_acertosb[vb] == ' P':
                       
                       pb = False

                    elif lista_acertosb[vb] == ' E':
                       
                       eb = False

                    elif lista_acertosb[vb] == ' C':
                       
                       cb = False

                    elif lista_acertosb[vb] == ' S':
                       
                       sb = False

                    if pb == False and eb == False and cb == False and sb == False:
                        tirosb = 21
                        print('CAMPO DO BOT')
                        imprime(Mbot,bot)
                        print('Voce perdeu\nO bot acertou todas as suas embarcações. MELHORE!!')
                        break
                turno = True
    
main()