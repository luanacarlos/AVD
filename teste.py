import random
import math

def variavel_aleatoria_exponencial(taxa):
    return -math.log(1.0 - random.random()) / taxa

def simulacao_fila_mm1(n, taxa_chegada, taxa_servico):
    relogio = 0.0
    fila = []
    tempos_de_espera_total = []

    for i in range(n):
        tempo_entre_chegadas = variavel_aleatoria_exponencial(taxa_chegada)
        relogio += tempo_entre_chegadas
        tempo_de_servico = variavel_aleatoria_exponencial(taxa_servico)
        
        if fila:
            tempo_de_espera = max(0, fila[0] - (relogio - tempo_de_servico))
            tempos_de_espera_total.append(tempo_de_espera)
        
        fila.append(relogio + tempo_de_servico)

        while fila and fila[0] <= relogio:
            fila.pop(0)

    return tempos_de_espera_total

taxa_chegada = 9.0  
taxa_servico = 10.0  

# Número de clientes
valores_de_n = [10**3]

for n in valores_de_n:
    tempos_de_espera = simulacao_fila_mm1(n, taxa_chegada, taxa_servico)
    print(tempos_de_espera)
    tempo_de_espera_medio = sum(tempos_de_espera) / n
    print(f"Número de clientes (n): {n}")
    print(f"Tempo Médio de Espera: {tempo_de_espera_medio:.6f} segundos\n")
