'''Alunos
Mateus Mota Nobrega - 21953021
Luan Cunha Loureiro de Alencar - 22051002
link para o jupyter: https://colab.research.google.com/drive/1zRz7BgfbjGz79Jw6BWTJTgQcI8nTiTWb?usp=sharing
'''

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math
import scipy.stats 


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
    return(round((numerador/denominador), 3))
    

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
    return[round((media_aritmetica(dados)-constante),6), round((media_aritmetica(dados)+constante), 6)]


def intervalo_de_confianca_menor_30(dados, nivel_de_confianca):
    confianca = (nivel_de_confianca/100)
    alpha = 1 - confianca
    alpha_barra = 1 - (alpha/2)
    t_student = scipy.stats.t.ppf(alpha_barra, (len(dados)-1))
    constante = constante = t_student * (desvio_padrao(dados) / (math.sqrt(len(dados))))
    return[round((media_aritmetica(dados)-constante), 6), round((media_aritmetica(dados)+constante), 6)]


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


def tamanho_de_amostra(desvio_padrao, largura, nivel_de_confianca):
    confianca = round((nivel_de_confianca/100),2)
    alpha = 1 - confianca
    alpha_barra = round(((1+confianca)/2), 3)
    z_score = scipy.stats.norm.ppf(alpha_barra)
    numerador = (((desvio_padrao*z_score)**2)*4)
    tamanho_amostra = (numerador/(largura**2))
    return int(tamanho_amostra)


def tamanho_de_amostra_por_precisao(desvio_padrao, nivel_de_confianca, precisao_percentual, media_estimada):
    z_score = scipy.stats.norm.ppf(1 - (1 - nivel_de_confianca) / 2)
    tamanho_amostra = math.ceil((100 * desvio_padrao * z_score) / (precisao_percentual * media_estimada))
    return tamanho_amostra


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


def valor_esperado_bernoulli(p):
    return 0 * (1 - p) + 1 * p


def variancia_bernoulli(p):
    return p * (1 - p)


def coeficiente_variacao_bernoulli(p):
    return math.sqrt(variancia_bernoulli(p)) / valor_esperado_bernoulli(p)


def probabilidade_binomial(n, k, p):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def valor_esperado_geometrica(p):
    return 1 / p


def variancia_geometrica(p):
    return (1 - p) / (p ** 2)


def coeficiente_variacao_geometrica(p):
    return math.sqrt(variancia_geometrica(p)) / (1 / p)


def probabilidade_retransmissao(p, i):
    return p * ((1 - p) ** (i - 1))


def valor_esperado_poisson(lambd):
    return lambd


def variancia_poisson(lambd):
    return lambd


def coeficiente_variacao_poisson(lambd):
    return math.sqrt(lambd) / lambd


def probabilidade_poisson(lambd, k):
    prob = sum((math.exp(-lambd) * (lambd ** i) / math.factorial(i)) for i in range(k + 1))
    return prob
