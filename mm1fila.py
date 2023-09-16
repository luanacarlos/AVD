import random
import math
import time
import numpy as np
from bib import intervalo_de_confianca

start = time.time()

def variavel_aleatoria_exponencial(taxa):
    return -math.log(1.0 - random.random()) / taxa

def gerador_tempos(n, taxa_chegada=1, taxa_servico=1):
    saida = []
    for i in range(n):
        saida.append([variavel_aleatoria_exponencial(taxa_chegada), variavel_aleatoria_exponencial(taxa_servico), 0])
    
    return saida


def simulador_mm1(n, taxa_chegada, taxa_servico):   
    tempos_aleatorios = [variavel_aleatoria_exponencial(taxa_chegada), variavel_aleatoria_exponencial(taxa_servico), 0]
    fila = []                                                               #onde esperam
    atendidos = np.zeros(n)                                                      #terminaram o atendimento
    em_servico = tempos_aleatorios
    clock = em_servico[0]
    iterador = 0
    chegada, servico, espera = 0.0, 0.0, 0.0


    while iterador < n or fila:
        if iterador < n:
            chegada = variavel_aleatoria_exponencial(taxa_chegada)
            servico = variavel_aleatoria_exponencial(taxa_servico)
            espera = 0


            if em_servico[1] > chegada:
                clock += chegada 
                em_servico[1] -= chegada 
                fila.append([chegada, servico, espera]) 
                fila[-1][2] = clock
                

            elif em_servico[1] == chegada:
                clock += chegada
                fila.append([chegada, servico, espera]) 
                fila[-1][2] = clock
                atendidos[iterador] = em_servico[2]
                em_servico = fila.pop(0)
                em_servico[2] = clock-em_servico[2]
                iterador += 1

            elif em_servico[1] < chegada:
                clock += em_servico[1]
                chegada -= em_servico[1]
                atendidos[iterador] = em_servico[2]
                iterador += 1

                if fila:
                    em_servico = fila.pop(0)
                    em_servico[2] = clock - em_servico[2]
                    
                
                else:
                    clock += chegada
                    em_servico = [chegada, servico, espera]
                    

            
        else:

            if fila:
                clock += em_servico[1]
                atendidos[-1] = em_servico[2]
                em_servico = fila.pop(0)
                em_servico[2] = clock - em_servico[2]
                
        
        
        
        
        
    #atendidos[iterador] = em_servico[2]
    
    
    return atendidos



tempos = simulador_mm1(10**5, 9, 10)
print(f'Valor de espera segundo teoria das filas = {9/10}')
print(f'Intervalo de Confiança = {intervalo_de_confianca(tempos, 95)}')
end = time.time()
print(f'Tempo de execução = {end-start} segundos')
print(f'Media de espera na fila = {sum(tempos)/len(tempos)}')