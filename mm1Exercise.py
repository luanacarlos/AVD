import random
import numpy as np
import math

def variavel_aleatoria_exponencial(taxa):
    return -math.log(1.0 - random.random()) / taxa

def simulacao_fila_mm1(n, taxa_chegada, taxa_servico):
    relogio = 0.0
    fila = []
    tempos_de_espera = []

    for i in range(n):
        tempo_entre_chegadas = variavel_aleatoria_exponencial(taxa_chegada)
        relogio += tempo_entre_chegadas
        tempo_de_servico = variavel_aleatoria_exponencial(taxa_servico)

        if fila:
            tempo_de_espera = max(0, fila[0] - (relogio - tempo_de_servico))
            tempos_de_espera.append(tempo_de_espera)

        fila.append(relogio + tempo_de_servico)
        while fila and fila[0] <= relogio:
            fila.pop(0)

    return tempos_de_espera

taxa_chegada = 9.0  
taxa_servico = 10.0  

# Número de clientes
valores_de_n = [10**3]

def calcular_intervalo_confianca(tempos_de_espera, n):
    tempo_de_espera_medio = sum(tempos_de_espera) / n
    intervalo_confianca = tempo_de_espera_medio, 1.96 * math.sqrt(tempo_de_espera_medio * (1 - tempo_de_espera_medio) / n)
    return intervalo_confianca

for n in valores_de_n:
    tempos_de_espera = simulacao_fila_mm1(n, taxa_chegada, taxa_servico)
    tempo_de_espera_medio, intervalo_confianca = calcular_intervalo_confianca(tempos_de_espera, n)
    print(f"Número de clientes (n): {n}")
    print(f"Tempo médio de espera: {tempo_de_espera_medio:.6f} segundos")
    print(f"Intervalo de confiança: {tempo_de_espera_medio:.6f} +- {intervalo_confianca:.6f} segundos")
