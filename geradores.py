from bib import *             # importar apenas as funcoes que serao utilizadas
import random         # Gerador de NA do Python
import math
from scipy.stats import chi2


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
        
def chi_squared_test(generator_output, k):
    # Gerar k intervalos igualmente espaçados entre 0 e 1
    intervals = np.linspace(0, 1, k+1)
    
    # Calcular as frequências observadas
    observed_frequencies = np.histogram(generator_output, bins=intervals)[0]
    
    # Calcular as frequências esperadas (uniformemente distribuídas)
    n = len(generator_output)
    expected_frequency = n / k
    
    expected_frequencies = np.array([expected_frequency] * k)
    
    # Calcular a estatística do qui-quadrado
    chi_squared = np.sum((observed_frequencies - expected_frequencies)**2 / expected_frequencies)
    
    # Calcular os graus de liberdade
    df = k - 1
    
    # Encontrar o valor crítico do qui-quadrado para alpha=0.05 e df graus de liberdade
    critical_value = chi2.ppf(0.95, df)
    
    # Comparar o valor calculado de chi_squared com o valor crítico
    if chi_squared < critical_value:
        return "Aceita a hipotese nula. Os números sao aleatórios."
    else:
        return "Rejeita a hipotese nula. Os números nao sao aleatórios."
    
# Parâmetros para o gerador G1
a1 = 12351
c1 = 1
m1 = 2**15
quantidade1 = 5000  # Ajuste a quantidade conforme necessário

# Gerar a sequência de números pseudoaleatórios
output1 = gerador_linear_congruencial(a1, c1, m1, quantidade1)

# Realizar o teste do qui-quadrado
k1 = 1000  # Número de intervalos
result1 = chi_squared_test(output1, k1)
print(result1)

  
#print(metodo_quadrado_central(1234, 30))
#numeros = gerador_linear_congruencial(25214903917, 11, 2**48, 5000)
#print(gerador_python(123, 100))

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

g1 = gerador_linear_congruencial(12351, 1, 2**15, 5000)
g5 = gerador_python(5000)

def gerar_variavel_exponencial(numeros_gerados):
    beta = 1/9
    index_aleatorio = random.randint(0, 4998)
    U = numeros_gerados[index_aleatorio]
    Va_exponencial = -beta * math.log(1 - U)

    return Va_exponencial

VA_exponencial_g1 = gerar_variavel_exponencial(g1)
VA_exponencial_g5 = gerar_variavel_exponencial(g5)

<<<<<<< HEAD
import math

def va_exponencial_com_g1(quantidade, a, c, m, taxa):
    g1 = gerador_linear_congruencial(a, c, m, quantidade)
    return [- (1 / taxa) * math.log(1 - u) for u in g1]

def va_exponencial_com_g5(quantidade, taxa):
    g5 = gerador_python(quantidade)
    return [- (1 / taxa) * math.log(1 - u) for u in g5]

# Parâmetros da distribuição exponencial
taxa = 0.5  # Substitua pela taxa desejada
quantidade = 5000  # Substitua pelo número desejado de amostras

# Usando g1 para gerar variáveis exponenciais
va_g1 = va_exponencial_com_g1(quantidade, 12351, 1, 2**15, taxa)

# Usando g5 para gerar variáveis exponenciais
va_g5 = va_exponencial_com_g5(quantidade, taxa)

=======

def gerar_variavel_exponencial(numeros_gerados, taxa_lambda):
    index_aleatorio = random.randint(0, 4998)
    numero_aleatorio = numeros_gerados[index_aleatorio]
    variavel_exponencial = -np.log(1 - numero_aleatorio) / taxa_lambda
    return variavel_exponencial
>>>>>>> 8ede1d854e4f04b67eb70c7dbc2934e384517943
