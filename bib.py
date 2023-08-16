import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import scipy.stats 
import math


def media_aritmetica(dados):
    return sum(dados)/len(dados) if len(dados) > 0 else 0


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
    return(round(media,1))


def media_geometrica(dados):
    media = np.prod(dados)**(1/len(dados))
    return(round(media, 1))


def media_harmonica(dados):
    numerador = len(dados)
    denominador = sum(list(map(lambda x : 1/x, dados)))
    return(round(numerador/denominador))
    

def media_das_taxas(media, taxa):
    media_1 = sum(list(media))/len(media)
    media_2 = sum(list(taxa))/len(taxa)
    return (round(((media_2/media_1)*100), 1))


def media_das_taxas_constante(dados_1, constante):
    soma = sum(list(dados_1))
    denominador = constante*len(dados_1)
    return(((1/denominador)*soma)*100)


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
    return variancia


def desvio_padrao(dados):
    variancia = variancia_amostral(dados)
    desvioPadrao = math.sqrt(variancia)
    return desvioPadrao


#Essa função ainda n funciona como deveria!! -> ta sim!!
def coeficiente_de_variacao(dados):
    desvio = desvio_padrao(dados)
    media = media_aritmetica(dados)
    coefieciente = (desvio/media) *100
    return coefieciente


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
    return[media_aritmetica(dados)-constante, media_aritmetica(dados)+constante]


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

    
def amostras_nao_pareadas(amostra_A, amostra_B, nivel_de_confianca):
    media_A =  media_amostral(amostra_A)
    media_B = media_amostral(amostra_B)
    diferenca_medias = media_A - media_B
    desvio_A = desvio_padrao(amostra_A)
    desvio_B = desvio_padrao(amostra_B)
    constante = ((desvio_A**2)/len(amostra_A)) + ((desvio_B**2)/len(amostra_B))
    desvio_das_diferencas = math.sqrt(constante)
    variavel_a = (1/(len(amostra_A)-1))*(((desvio_A**2)/len(amostra_A)))
    variavel_b = (1/(len(amostra_B)-1))*(((desvio_B**2)/len(amostra_B)))
    graus_de_liberdade = (int)(((constante**2)/(variavel_a+variavel_b))-2)
    confianca = (nivel_de_confianca/100)
    alpha = 1 - confianca
    alpha_barra = 1 - (alpha/2)
    return [diferenca_medias - (desvio_das_diferencas*scipy.stats.t.ppf(graus_de_liberdade, alpha_barra)),
            diferenca_medias + (desvio_das_diferencas*scipy.stats.t.ppf(graus_de_liberdade, alpha_barra))]



sistema_A = [5.4, 16.6, 0.6, 1.4, 0.6, 7.3]
sistema_B = [19.1, 3.5, 3.4, 2.5, 3.6, 1.7]
teste_media_zero(intervalo_de_confianca(subtrai_sistemas(sistema_A, sistema_B), 90)) 
teste_media_zero(subtrai_sistemas(sistema_A, sistema_B), 95) 
teste_media_zero(subtrai_sistemas(sistema_A, sistema_B), 99)

exercicio_dois = [1.5, 2.6, -1.8, 1.3, -0.5, 1.7, 2.4] 
teste_media_zero(exercicio_dois, 99)


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
print(resultado)



