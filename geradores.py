from bib import *             # importar apenas as funcoes que serao utilizadas
import random         # Gerador de NA do Python


def preenche_digitos(numero):
    numero = str(numero)
    return numero.zfill(8)


def trata_numero(numero):
    if len(str(numero)) > 8:
        return str(numero)[:8:]
    else:
        return str(numero)


def metodo_quadrado_central(z0, quantidade):
    lista = []
    iteracoes = 0
    while iteracoes < quantidade:
        z0 = trata_numero((z0**2)) if len(str(z0**2)) >= 8 else preenche_digitos(z0**2)
        z1 = str(z0[2:6:])
        z0 = int(z1)
        z1 = int(z1) / 10000.0
        lista.append(z1)
        iteracoes += 1
    
    return lista
    
    
def gerador_linear_congruencial(a, c, m, quantidade):
    if quantidade <= m:
        lista = []
        iteracoes = 0
        while iteracoes < quantidade:
            n =  ((a*iteracoes) + c)%m 
            lista.append(n/m)
            iteracoes += 1
        
        return lista

    else: 
        print('Não é possivel gerar essa quantidade de numeros com os parametros dados')
        
def gerador_python(semente, quantidade):
    iteracoes = 0
    lista = []
    numero = 0
    random.seed(semente)
    while iteracoes < quantidade:
        numero = random.random()
        lista.append(numero)
        iteracoes += 1
        
    return lista
        
    
  
#print(metodo_quadrado_central(1234, 30))
#numeros = gerador_linear_congruencial(25214903917, 11, 2**48, 5000)
print(gerador_python(123, 100))

"""import matplotlib.pyplot as plt


# Criar um gráfico de linha
plt.plot(numeros)

# Adicionar rótulos aos eixos x e y
plt.xlabel('Índice')
plt.ylabel('Números')

# Adicionar um título ao gráfico
plt.title('Gráfico de Números')

# Mostrar o gráfico
plt.show()
"""