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

#implementar de modo que ja receba um array def plotar_histograma(array):
def plotar_histograma():
    frequencias = [int(item) for item in input("Digite as frequencias : ").split()]
    plt.hist(frequencias, rwidth=0.5)
    plt.show()

plotar_histograma()