import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from collections import Counter
import math

constantes_de_confianca = {80: 1.28, 85: 1.44, 90: 1.64, 95: 1.96, 99: 2.57, 99.5: 2.8, 99.9: 3.29}

def media_aritmetica(dados):
    soma = 0
    for i in dados:
        soma += i

    return soma/len(dados) if len(dados) > 0 else 0


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
    

def media_das_taxas(dados_1, dados_2):
    taxa_1 = sum(list(dados_1))/len(dados_1)
    taxa_2 = sum(list(dados_2))/len(dados_2)
    return (round(((taxa_1/taxa_2)*100), 1))


def media_das_taxas_constante(dados_1, constante):
    soma = sum(list(dados_1))
    denominador = constante*len(dados_1)
    return(((1/denominador)*soma)*100)


def moda(dados):
    return(max(set(dados), key=dados.count))


#implementar de modo que ja receba um array def plotar_histograma(array):
def plotar_histograma():
    frequencias = [int(item) for item in input("Digite as frequencias : ").split()]
    plt.hist(frequencias, rwidth=0.5)
    plt.show()


def amplitude (dados):
    return max(dados) - min(dados)


def media_amostral(dados):
    soma = sum(dados)
    tamanho = len(dados)
    return soma/tamanho


def variancia_amostral(dados):
    n = len(dados)
    media = media_aritmetica(dados)
    soma_diferencas_quad = np.sum(np.fromiter(((x - media) * (x - media) for x in dados), dtype=float))
    variancia = soma_diferencas_quad / n
    return round(variancia)


def desvio_padrao (dados):
    variancia = variancia_amostral(dados)
    desvioPadrao = math.sqrt(variancia)
    return round(desvioPadrao)


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
    constante = constantes_de_confianca[nivel_de_confianca]*desvio_padrao(dados)
    return[media_aritmetica(dados)-constante, media_aritmetica(dados)+constante]





idadePessoas = [460, 800, 300, 400]

print(variancia_amostral(idadePessoas))
print(desvio_padrao(idadePessoas))
print(media_aritmetica(idadePessoas))
print(intervalo_de_confianca_maior_30)

print(coeficiente_de_variacao(idadePessoas))

amostra = [10, 15, 20, 25, 30, 35, 40, 45, 50]
q1, q2, q3 = calcular_quartis(amostra)
print("Primeiro Quartil (Q1):", q1)
print("Segundo Quartil (Q2, Mediana):", q2)
print("Terceiro Quartil (Q3):", q3)

print(amplitude_interquartil(amostra))