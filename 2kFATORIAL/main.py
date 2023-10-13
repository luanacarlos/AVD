def tabela_de_sinais_2 (k, repeticoes):
    # criar tabela de sinais para k = 2
    tabela = []
    for i in range(k):
        for j in range(k):
            linha = [1, i, j, i * j]
            if repeticoes > 1:
                linha.append((0,) * repeticoes)
            else:
                linha.append(0)
            tabela.append(linha)
    return tabela



def imprimir_tabela_2(tabela):
    print("{:^5} {:^5} {:^5} {:^5} {:^5}".format("1","A", "B", "AB", "Y"))
    for linha in tabela:
        print("{:^5} {:^5} {:^5} {:^5} {:^5}".format(linha[0], linha[1], linha[2],  linha[3], linha[4]))

def tabela_de_sinais_2():
    tabela = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            linha = [1, j, i]
            linha.append(linha[1] * linha[2]) # AB
            linha.append(0) # Y
            tabela.append(linha)
    return tabela

# Chamar as funções para criar e imprimir a tabela de sinais
tabela = tabela_de_sinais_2()
imprimir_tabela_2(tabela)

for linha in tabela:
    print(linha)
