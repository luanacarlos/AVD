import itertools 

##FUNCAO PARA CALCULAR OS RESULTADOS E COLOCAR NA TABELA - REPETIÇÔES 
def adicionar_resultado_repeat_1 (tabela):
    y = []
    
    # Multiplicar a coluna Y pela coluna 1
    sum = 0
    for i, linha in enumerate(tabela):
        sum = sum + (tabela[i][-1] * linha[0])
    y.append(sum)

    #COLUNA A*Y 
    sum = 0
    for i, linha in enumerate(tabela):
        sum = sum + (tabela[i][-1] * linha[1])
    y.append(sum)

    #COLUNA B*Y
    sum = 0
    for i, linha in enumerate(tabela):
        sum = sum + (tabela[i][-1] * linha[2])
    y.append(sum)

    #COLUNA AB*Y
    sum = 0
    for i, linha in enumerate(tabela):
        sum = sum + (tabela[i][-1] * linha[3])
    y.append(sum)

    #SÓ COLOCAR TOTAL lA MESMO
    y.append("Total")
    tabela.append(y)
    
    #lINHA ABAIXO QUE TEM OS RESULTAODS DIVIDIDO POR 4
    new_y = []
    for i in range (len(y)-1):
        new_y.append(y[i] /4)
    new_y.append("Total/4")
    tabela.append(new_y)  
    
    

# PARA K = 2
def imprimir_tabela_2_repeat_1(tabela):
    print("\n----------Tabela De Sinais--------------\n")
    print("{:^5} {:^5} {:^5} {:^5} {:^5}".format("1","A", "B", "AB", "Y"))
    for linha in tabela:
        print("{:^5} {:^5} {:^5} {:^5} {:^5}".format(linha[0], linha[1], linha[2],  linha[3], str(linha[4])))

def imprimir_tabela_2_repeat_maior1(tabela):
    print("{:^5} {:^5} {:^5} {:^5} {:^5} {:^25}".format("1", "A", "B", "AB", "Y", "yMedia"))
    for linha in tabela:
        if len(linha) >= 6:
            print("{:^5} {:^5} {:^5} {:^5} {:^5} {:^10}".format(linha[0], linha[1], linha[2], linha[3], str(linha[4]), linha[5]))

def tabela_de_sinais_2(repeticoes):
    tabela = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            linha = [1, j, i]
            linha.append(linha[1] * linha[2]) # AB
            if repeticoes > 2:
                # count = 0
                # while(count<repeticoes):
                a = [15,18,12]
                    # x = int(input("Digite o valor de resultados: "))
                    # a.append(x)
                    # count = count + 1  
                linha.append(a) # Y(1,2,3,4,5,6,7,8)
            else:
                x = int(input("Digite o valor de resultados: "))
                linha.append(x) # Y
            tabela.append(linha)
    return tabela

# Adicionar resultados - Repeticoes maior que 1
def calcula_yMedia(tabela, repeticoes):
    soma_y = 0
    for linha in tabela:
        if len(linha) > 4: #Coluna Y
            soma_y = sum(linha[4])/ repeticoes
            linha.append(soma_y) #Coluna Y Media


k = int(input("Digite o valor de K: "))
repeticoes = int(input("Digite o valor de repeticoes: "))
if k == 2:
    if repeticoes == 1:
        tabela = tabela_de_sinais_2(repeticoes)
        adicionar_resultado_repeat_1(tabela)
        imprimir_tabela_2_repeat_1(tabela)
    else:
        tabela = tabela_de_sinais_2(repeticoes)
        calcula_yMedia(tabela, repeticoes)
        imprimir_tabela_2_repeat_maior1(tabela)
else:
    print("TODO()")

# PARA K = 3
def tabela_de_sinais3(k,repeticoes):
    tabela = []
    for i, j, x in itertools.product([-1, 1], repeat=k):
        linha = [1, x, j, i]
        linha.append(linha[1] * linha[2])              # AB
        linha.append(linha[1] * linha[3])              # AC
        linha.append(linha[2] * linha[3])              # BC
        linha.append(linha[1] * linha[2] * linha[3])   # ABC
        if repeticoes > 1:
            linha.append((0,) * repeticoes) #Y()
        else:
            linha.append(0)      
        tabela.append(linha) # Y
    return tabela



def imprimir_tabela_3(tabela):
    print("\n----------Tabela De Sinais--------------\n")
    print ("{:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5}".format("1","A", "B", "C", "AB", "AC", "BC", "ABC", "Y"))
    for linha in tabela:
        print ("{:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5}".format(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8]))


