import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import scipy.stats 
import math


def media_aritmetica(dados):
    return round((sum(dados)/len(dados)),3) if len(dados) > 0 else 0


def mediana(dados):
    dados.sort()
    if len(dados)%2 == 0:
        return media_aritmetica([dados[len(dados)/2],dados[(len(dados)/2)+1]])  
    else:
        index = round(len(dados)/2) 
        return (dados[index-1])


def media_ponderada(dados, pesos):
    numerador = sum(list(map(lambda x, y: x*y, pesos, dados)))
    media = numerador/sum(pesos)
    return(round(media,3))


def media_geometrica(dados):
    media = np.prod(dados)**(1/len(dados))
    return(round(media, 1))


def media_harmonica(dados):
    numerador = len(dados)
    denominador = sum(list(map(lambda x : 1/x, dados)))
    return(round(numerador/denominador), 3)
    

def media_das_taxas(media, taxa):
    media_1 = sum(list(media))/len(media)
    media_2 = sum(list(taxa))/len(taxa)
    return (round(((media_2/media_1)*100), 3))


def media_das_taxas_constante(dados_1, constante):
    soma = sum(list(dados_1))
    denominador = constante*len(dados_1)
    return(round((((1/denominador)*soma)*100), 3))


def moda(dados):
    return(max(set(dados), key=dados.count))


#implementar de modo que ja receba um array def plotar_histograma(array):
#def plotar_histograma():
 #   frequencias = [int(item) for item in input("Digite as frequencias : ").split()]
  #  plt.hist(frequencias, rwidth=0.5)
   # plt.show()


def amplitude (dados):
    return (max(dados) - min(dados))


def media_amostral(dados):
    return media_aritmetica(dados)


def variancia_amostral(dados):
    n = len(dados)
    media = media_aritmetica(dados)
    soma_diferencas_quad = np.sum(np.fromiter(((x - media) * (x - media) for x in dados), dtype=float))
    variancia = soma_diferencas_quad / n
    return round(variancia, 3)


def desvio_padrao(dados):
    variancia = variancia_amostral(dados)
    desvioPadrao = math.sqrt(variancia)
    return round(desvioPadrao, 3)


#Essa função ainda n funciona como deveria!! -> ta sim!!
def coeficiente_de_variacao(dados):
    desvio = desvio_padrao(dados)
    media = media_aritmetica(dados)
    coefieciente = (desvio/media) *100
    return round(coefieciente, 3)


def calcular_quartis(dados):
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)
    quartil_1 = dados_ordenados[int(n * 0.25)]
    quartil_2 = dados_ordenados[int(n * 0.5)]
    quartil_3 = dados_ordenados[int(n * 0.75)]
    return quartil_1, quartil_2, quartil_3


def amplitude_interquartil(dados):
    q1,q2,q3 = calcular_quartis(dados)
    a = q1
    b= q3
    return b-a


def intervalo_de_confianca_maior_30(dados, nivel_de_confianca):
    confianca = (nivel_de_confianca/100)
    alpha = 1 - confianca
    alpha_barra = 1 - (alpha/2)
    distribuicao_normal = scipy.stats.norm.ppf(alpha_barra)
    constante = distribuicao_normal*desvio_padrao(dados)/(math.sqrt(len(dados)))
    return[round((media_aritmetica(dados)-constante),3), round((media_aritmetica(dados)+constante), 3)]


def intervalo_de_confianca_menor_30(dados, nivel_de_confianca):
    confianca = (nivel_de_confianca/100)
    alpha = 1 - confianca
    alpha_barra = 1 - (alpha/2)
    t_student = scipy.stats.t.ppf(alpha_barra, (len(dados)-1))
    constante = t_student*(desvio_padrao(dados)/(math.sqrt(len(dados))))
    return[round((media_aritmetica(dados)-constante), 3), round((media_aritmetica(dados)+constante), 3)]


def intervalo_de_confianca(dados, nivel_de_confianca):
    if len(dados) >= 30:
        return intervalo_de_confianca_maior_30(dados, nivel_de_confianca)
    
    else:
        return intervalo_de_confianca_menor_30(dados, nivel_de_confianca)
    


def subtrai_sistemas(sistema_A, sistema_B):
    return list(map(lambda x, y: x - y, sistema_A, sistema_B))
    

def teste_media_zero(intervalo):
    limite_inferior = intervalo[0]
    limite_superior = intervalo[1]
    if limite_inferior <= 0 <= limite_superior:
        print(f'Não há diferença significativa entre os sistemas pois como vemos no intervalo {intervalo}, o 0 está incluso')
        
    else:
        print(f'Há diferença entre os dois sistemas pois como vemos {intervalo}, o 0 não está incluso')

    
def intervalo_nao_paralelo(diferenca_amostral, diferenca_desvio_padrao, grau_liberdade, nivel_de_confianca):
    confianca = round((nivel_de_confianca/100),2)
    alpha = 1 - confianca
    alpha_barra = round(((1+confianca)/2), 3)
    print(f'alpga barra {alpha_barra}')
    print(scipy.stats.t.ppf(alpha_barra, abs(grau_liberdade)))
    return [(diferenca_amostral - (diferenca_desvio_padrao*scipy.stats.t.ppf(alpha_barra, abs(grau_liberdade)))), 
            (diferenca_amostral + (diferenca_desvio_padrao*scipy.stats.t.ppf(alpha_barra, abs(grau_liberdade))))]


def amostras_nao_pareadas(amostra_A, amostra_B, nivel_de_confianca):
    media_amostral_A = media_amostral(amostra_A)
    media_amostral_B = media_amostral(amostra_B)
    diferenca_media_amostral = (media_amostral_A - media_amostral_B)
    desvio_padrao_A = desvio_padrao(amostra_A)
    desvio_padrao_B = desvio_padrao(amostra_B)
    constante_A = round(((desvio_padrao_A**2)/len(amostra_A)), 3)
    constante_B = round(((desvio_padrao_B**2)/len(amostra_B)), 3)
    desvio_padrao_das_diferencas = round((math.sqrt(constante_A+constante_A)),3)
    numerador_liberdade = (constante_A+constante_B)**2
    variavel_A = abs(round(((1/len(amostra_A)-1)*(constante_A**2)), 3))
    variavel_B = abs(round(((1/len(amostra_B)-1)*(constante_B**2)), 3))
    grau_de_liberdade = round((numerador_liberdade/(variavel_A+variavel_B)))
    return intervalo_nao_paralelo(diferenca_media_amostral, desvio_padrao_das_diferencas, grau_de_liberdade, nivel_de_confianca)


#TAMANHO DE UMA AMOSTRA
def tamanho_de_amostra(desvio_padrao, largura, nivel_de_confianca):
    confianca = round((nivel_de_confianca/100),2)
    alpha = 1 - confianca
    alpha_barra = round(((1+confianca)/2), 3)
    z_score = scipy.stats.norm.ppf(alpha_barra)
    numerador = (((desvio_padrao*z_score)**2)*4)
    tamanho_amostra = (numerador/(largura**2))
    return int(tamanho_amostra)


print(tamanho_de_amostra(desvio_padrao=6, nivel_de_confianca=95, largura=3))

"""
def tamanho_amostra_com_precisao(media_amostral, desvio_padrao, precisao, nivel_de_confianca):
    intervalo_inferior = round((media_amostral*(1-(precisao/100))), 3)
    intervalo_superior = round((media_amostral*(1+(precisao/100))), 3)
    largura =
    return [intervalo_inferior, intervalo_superior]

"""


def calcula_distribuicao_normal_cdf(z):
    t = 1.0 / (1.0 + 0.2316419 * abs(z))
    coeficientes = [0.31938153, -0.356563782, 1.781477937, -1.821255978, 1.330274429]
    cdf = 1.0 - 1.0 / math.sqrt(2*math.pi) * math.exp(-z**2 / 2.0) * (coeficientes[0]*t + coeficientes[1]*t**2 + coeficientes[2]*t**3 + coeficientes[3]*t**4 + coeficientes[4]*t**5)
    return cdf

def teste_hipotese_z(media_amostral, media_nula, desvio_padrao_populacional, tamanho_amostra, nivel_significancia, alternativa='dois-lados'):

    escore_z = (media_amostral - media_nula) / (desvio_padrao_populacional / math.sqrt(tamanho_amostra))
    
    if alternativa == 'dois-lados':
        valor_p = 2 * (1 - calcula_distribuicao_normal_cdf(abs(escore_z)))
    elif alternativa == 'menor':
        valor_p = calcula_distribuicao_normal_cdf(escore_z)
    elif alternativa == 'maior':
        valor_p = 1 - calcula_distribuicao_normal_cdf(escore_z)
    else:
        raise ValueError("Hipótese alternativa inválida")
    
    if valor_p < nivel_significancia:
        return "Rejeitar a hipótese nula"
    else:
        return "Não rejeitar a hipótese nula"


# Parâmetros
media_amostral = 43
media_nula = 45
desvio_padrao_populacional = 6
tamanho_amostra = 64
nivel_significancia = 0.10
alternativa = 'dois-lados'

# Chamada da função
resultado = teste_hipotese_z(media_amostral, media_nula, desvio_padrao_populacional, tamanho_amostra, nivel_significancia, alternativa)
#print(resultado)


'''
amostra_A = [5.3, 16, 0.6, 1.4, 0.6, 7.7, 3.6, 2.4, 12,
             6, 57, 2, 1, 4, 6, 4, 8, 1]

amostra_B = [19, 3.5, 3.3, 2.5, 3.6, 1.7, 12, 2, 8, 1, 1, 4]

print(amostras_nao_pareadas(amostra_A, amostra_B, 95) )
intervalo = amostras_nao_pareadas(amostra_A, amostra_B, 95)
print(intervalo)
print(teste_media_zero(intervalo))



sistema_A = [5.4, 16.6, 0.6, 1.4, 0.6, 7.3]
sistema_B = [19.1, 3.5, 3.4, 2.5, 3.6, 1.7]
teste_media_zero(intervalo_de_confianca(subtrai_sistemas(sistema_A, sistema_B), 90)) 
teste_media_zero(subtrai_sistemas(sistema_A, sistema_B), 95) 
teste_media_zero(subtrai_sistemas(sistema_A, sistema_B), 99)

exercicio_dois = [1.5, 2.6, -1.8, 1.3, -0.5, 1.7, 2.4] 
teste_media_zero(exercicio_dois, 99)
'''

# -------------- INICIO LIBS DE CONCEITOS DE PROBABILIDADE --------------


def calcular_valor_esperado_VA_discreta(valores, probabilidades):
    if len(valores) != len(probabilidades):
        raise ValueError("Os tamanhos das listas de valores e probabilidades devem ser iguais.")
    
    valor_esperado = 0
    for i in range(len(valores)):
        valor_esperado += valores[i] * probabilidades[i]
    
    return valor_esperado


def calcular_esperanca(probabilidades, valores):
    esperanca = sum(p * x for p, x in zip(probabilidades, valores))
    return esperanca

def calcular_variancia(probabilidades, valores, esperanca):
    esperanca_quadrada = sum(p * x**2 for p, x in zip(probabilidades, valores))
    variancia = esperanca_quadrada - esperanca**2
    return variancia

# Distribuição de probabilidade
probabilidades = [1/4, 1/8, 1/8, 1/2]
valores = [2, 1, 2, 3]

# Calculando a esperança
esperanca = calcular_esperanca(probabilidades, valores)

# Calculando a variância
variancia = calcular_variancia(probabilidades, valores, esperanca)



#Exercicio slide 105 
import math 

def calcula_media_varianca_VA(dados_x, dados_p) :
    media  = sum(x * p for x, p in zip(dados_x, dados_p))
    variancia = sum((x - media) ** 2 * p for x, p in zip(dados_x, dados_p))
    
    return media, variancia

"""
dados_x = [16, 17, 18, 19, 20, 21, 22]
dados_p = [0.05, 0.10, 0.15, 0.25, 0.20, 0.15, 0.10]

media, variancia = calcula_media_varianca_VA(dados_x, dados_p)

std_deviation = math.sqrt(variancia)

print(f"medida (Esperança): {media:.2f}")
print(f"variancia: {variancia:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")

"""

#Exercicio Slide 106
#a)
p_4 = 0.05 # P(y) associada a y = 2 (2 * 2 = 4)
print(f"p(4): {p_4:.2f}")

#b)P(1 <= Y <= 16) 
p_values = [0.01, 0.05, 0.25, 0.35, 0.30]
y_values = [0, 1, 4, 9, 16]

p_interval = sum(p for y, p in zip(y_values, p_values) if 1 <= y <= 16)
print(f"P(1 <= Y <= 16): {p_interval:.2f}")


#c) P(1 < Y < 16)
p_interval_exclusive = sum(p for y, p in zip(y_values, p_values) if 1 < y < 16)
print(f"P(1 < Y < 16): {p_interval_exclusive:.2f}")

#até o slide 123

#Variável Aleatória de Bernoulli 

import math

def valor_esperado_bernoulli(p):
    return 0 * (1 - p) + 1 * p

def variancia_bernoulli(p):
    return p * (1 - p)

def coeficiente_variacao_bernoulli(p):
    return math.sqrt(variancia_bernoulli(p)) / valor_esperado_bernoulli(p)

# Parâmetro p da variável Bernoulli
p = 0.3

# Calculando e imprimindo os resultados
esperanca = valor_esperado_bernoulli(p)
variancia = variancia_bernoulli(p)
coef_variacao = coeficiente_variacao_bernoulli(p)

print(f"Valor Esperado (E[X]): {esperanca}")
print(f"Variancia (Var[X]): {variancia}")
print(f"Coeficiente de Variacao (CV[X]): {coef_variacao}")

#Variável Aleatória Binomial

import math

def calcular_valor_esperado(n, p):
    valor_esperado = n * p
    return valor_esperado

def calcular_variancia(n, p):
    variancia = n * p * (1 - p)
    return variancia

def calcular_coeficiente_variacao(n, p):
    coeficiente_variacao = math.sqrt(n * p * (1 - p)) / n
    return coeficiente_variacao

# Parâmetros da distribuição binomial
n = 10  # Número de tentativas
p = 0.3  # Probabilidade de sucesso

# Calculando o valor esperado
esperanca = calcular_valor_esperado(n, p)
print("Valor Esperado:", esperanca)

# Calculando a variância
variancia = calcular_variancia(n, p)
print("Variância:", variancia)

# Calculando o coeficiente de variação
coef_variacao = calcular_coeficiente_variacao(n, p)
print("Coeficiente de Variação:", coef_variacao)




#exemplo slide 114
import math

def probabilidade_binomial(n, k, p):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Parâmetros do problema
n = 10
k = 6
p = 0.75

# Calculando a probabilidade
probabilidade = probabilidade_binomial(n, k, p)

print(f"A probabilidade de exatamente {k} estudantes usarem notebook eh {probabilidade:.4f}")

#Variável Aleatória Geométrica

import math

def valor_esperado_geometrica(p):
    return 1 / p

def variancia_geometrica(p):
    return (1 - p) / (p ** 2)

def coeficiente_variacao_geometrica(p):
    return math.sqrt(variancia_geometrica(p)) / (1 / p)

# Parâmetro p da variável geométrica
p = 0.3

# Calculando e imprimindo os resultados
esperanca = valor_esperado_geometrica(p)
variancia = variancia_geometrica(p)
coef_variacao = coeficiente_variacao_geometrica(p)

print(f"Valor Esperado (E[X]): {esperanca}")
print(f"Variância (Var[X]): {variancia}")
print(f"Coeficiente de Variação (CV[X]): {coef_variacao}")

#exemplo slide 118 
def probabilidade_retransmissao(p, i):
    return p * ((1 - p) ** (i - 1))

# Parâmetros do problema
p = 0.9

# Calculando e imprimindo as probabilidades de retransmissão
for i in range(1, 4):
    prob = probabilidade_retransmissao(p, i)
    print(f"Probabilidade de retransmissão em {i} vezes: {prob:.4f}")

#Variável Aleatória Poisson 
import math

def valor_esperado_poisson(lambd):
    return lambd

def variancia_poisson(lambd):
    return lambd

def coeficiente_variacao_poisson(lambd):
    return math.sqrt(lambd) / lambd

# Parâmetro lambda da distribuição de Poisson
lambd = 3.0

# Calculando e imprimindo os resultados
esperanca = valor_esperado_poisson(lambd)
variancia = variancia_poisson(lambd)
coef_variacao = coeficiente_variacao_poisson(lambd)

print(f"Valor Esperado (E[X]): {esperanca}")
print(f"Variância (Var[X]): {variancia}")
print(f"Coeficiente de Variação (CV[X]): {coef_variacao}")




#Exemplo slide 122
def probabilidade_poisson(lambd, k):
    prob = sum((math.exp(-lambd) * (lambd ** i) / math.factorial(i)) for i in range(k + 1))
    return prob

# Parâmetros do problema
lambd = 2  # Fluxo de chegadas por minuto
k = 3  # Número máximo de jobs desejado

# Calculando e imprimindo a probabilidade
prob_max_tres_jobs = probabilidade_poisson(lambd, k)

print(f"Probabilidade de chegarem no máximo três jobs: {prob_max_tres_jobs:.4f}")
