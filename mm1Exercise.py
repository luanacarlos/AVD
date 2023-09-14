import numpy as np
import scipy
from bib import *
import random

def variavel_aleatoria_exponencial(taxa):
    return -math.log(1.0 - random.random()) / taxa

def simulacao_fila_mm1(n, taxa_chegada, taxa_servico):
    relogio = 0.0
    fila = []
    tempo_de_espera_total = 0


    for i in range(n):
        tempo_entre_chegadas = variavel_aleatoria_exponencial(taxa_chegada)
        relogio += tempo_entre_chegadas
        tempo_de_servico = variavel_aleatoria_exponencial(taxa_servico)
        
        if fila:
            tempo_de_espera = max(0, fila[0] - (relogio - tempo_de_servico))
            tempo_de_espera_total += tempo_de_espera

        
        fila.append(relogio + tempo_de_servico)

        while fila and fila[0] <= relogio:
            fila.pop(0)

    return tempo_de_espera_total


def intervalo_de_confianca(dados, nivel_de_confianca):
    confianca = (nivel_de_confianca/100)
    alpha = 1 - confianca
    alpha_barra = 1 - (alpha/2)
    distribuicao_normal = scipy.stats.norm.ppf(alpha_barra)
    constante = distribuicao_normal*desvio_padrao(dados)/(math.sqrt(len(dados)))
    return[round((media_aritmetica(dados)-constante),9), round((media_aritmetica(dados)+constante), 9)]


def main():
    n = 1000000
    taxa_chegada = 9
    taxa_servico = 10
    tempos_de_espera = simulacao_fila_mm1(n, taxa_chegada, taxa_servico)
    media = tempos_de_espera / n
    #interval_de_confianca = intervalo_de_confianca(tempos_de_espera, 99)
    print("Média aritmética:", media)
    #print("Intervalo de confiança:", interval_de_confianca)


if __name__ == "__main__":
    main()
