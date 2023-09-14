import random
import math
import time

start = time.time()

def variavel_aleatoria_exponencial(taxa):
    return -math.log(1.0 - random.random()) / taxa

def gerador_tempos(n, taxa_chegada=1, taxa_servico=1):
    saida = []
    for i in range(n):
        saida.append([variavel_aleatoria_exponencial(taxa_chegada), variavel_aleatoria_exponencial(taxa_servico), 0])
    
    return saida


def simulador_mm1(n, taxa_chegada, taxa_servico):
    fila = []                                                               #onde esperam
    tempos_aleatorios = gerador_tempos(n, taxa_chegada, taxa_servico)
    atendidos = []                                                          #terminaram o atendimento
    em_servico = tempos_aleatorios.pop(0)
    clock = em_servico[0]


    while tempos_aleatorios or fila:
        if tempos_aleatorios and em_servico[1] > tempos_aleatorios[0][0]:
            clock += tempos_aleatorios[0][0] 
            em_servico[1] -= tempos_aleatorios[0][0] 
            fila.append(tempos_aleatorios.pop(0)) 
            fila[-1][2] = clock

        elif tempos_aleatorios and em_servico[1] == tempos_aleatorios[0][0]:
            clock += tempos_aleatorios[0][0] 
            fila.append(tempos_aleatorios.pop(0)) 
            fila[-1][2] = clock
            atendidos.append(em_servico[2])
            em_servico = fila.pop(0)
            em_servico[2] = clock-em_servico[2]

        elif tempos_aleatorios and em_servico[1] < tempos_aleatorios[0][0]:
            clock += em_servico[1]
            tempos_aleatorios[0][0] -= em_servico[1]
            atendidos.append(em_servico[2])

            if fila:
                em_servico = fila.pop(0)
                em_servico[2] = clock - em_servico[2]
            
            else:
                clock += tempos_aleatorios[0][0]
                em_servico = tempos_aleatorios.pop(0)

        elif not tempos_aleatorios and fila:
            clock += em_servico[1]
            atendidos.append(em_servico[2])
            em_servico = fila.pop(0)
            em_servico[2] = clock - em_servico[2]
    
    atendidos.append(em_servico[2])
    
    return atendidos



print(simulador_mm1(10**8, 9, 10))
end = time.time()
print(f'Tempo de execução = {end-start} segundos')