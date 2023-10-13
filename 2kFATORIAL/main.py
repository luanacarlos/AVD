import itertools 

# PARA K = 2
def imprimir_tabela_2(tabela):
    print("{:^5} {:^5} {:^5} {:^5} {:^5}".format("1","A", "B", "AB", "Y"))
    for linha in tabela:
        print("{:^5} {:^5} {:^5} {:^5} {:^5}".format(linha[0], linha[1], linha[2],  linha[3], str(linha[4])))

def tabela_de_sinais_2():
    repeticoes = 1
    tabela = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            linha = [1, j, i]
            linha.append(linha[1] * linha[2]) # AB
            if repeticoes > 1:
                x = int(input("Digite o valor de resultados: "))
                linha.append((x,) * repeticoes) # Y(1,2,3,4,5,6,7,8)
            else:
                x = int(input("Digite o valor de resultados: "))
                linha.append(x) # Y
            tabela.append(linha)
    return tabela

##FUNCAO PARA CALCULAR OS RESULTADOS E COLOCAR NA TABELA
def adicionar_resultado (tabela):
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

# #Tabela atual - pre resultados
# tabela = tabela_de_sinais_2()
# imprimir_tabela_2(tabela)


# adicionar_resultado(tabela)
# imprimir_tabela_2(tabela) 



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
    print ("{:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5}".format("1","A", "B", "C", "AB", "AC", "BC", "ABC", "Y"))
    for linha in tabela:
        print ("{:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5}".format(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8]))



