import numpy as np
from numpy import *
import matplotlib.pyplot as plt


def media_aritmetica(dados):
    soma = 0
    for i in dados:
        soma += i

    return soma/len(dados) if len(dados) > 0 else 0


def mediana(dados):
    dados.sort()
    if len(dados)%2 == 0:
        return media([dados[len(dados)/2],dados[(len(dados)/2)+1]])  
    else:
        return dados(len)


def media_ponderada(pesos, dados):
    numerador = sum(list(map(lambda x, y: x*y, pesos, dados)))
    media = numerador/sum(pesos)
    print(round(media, 1))


def media_geometrica(dados):
    media = np.prod(dados)**(1/len(dados))
    print(round(media, 1))


def media_harmonica(dados):
    numerador = len(dados)
    denominador = sum(list(map(lambda x : 1/x, dados)))
    print(round(numerador/denominador))
    

def media_das_taxas(dados_1, dados_2):
    taxa_1 = sum(list(dados_1))/len(dados_1)
    taxa_2 = sum(list(dados_2))/len(dados_2)
    print (round(((taxa_1/taxa_2)*100), 1))


def media_das_taxas_constante(dados_1, constante):
    soma = sum(list(dados_1))
    denominador = constante*len(dados_1)
    print(((1/denominador)*soma)*100)


#implementar de modo que ja receba um array def plotar_histograma(array):
def plotar_histograma():
    frequencias = [int(item) for item in input("Digite as frequencias : ").split()]
    plt.hist(frequencias, rwidth=0.5)
    plt.show()


media_das_taxas_constante([3.0, 5.0, 4.2, 5.2, 8.6], 100)