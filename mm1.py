import random
import math
import time
import numpy as np
from bib import intervalo_de_confianca

'''
      o Cenário    I:  λ=7 clientes por segundo; μ=10 clientes por segundo.
      o Cenário   II:  λ=8 clientes por segundo; μ=10 clientes por segundo.
      o Cenário  III:  λ=9 clientes por segundo; μ=10 clientes por segundo.
      o Cenário   IV:  λ=9,5 clientes por segundo; μ=10 clientes por segundo.
'''



def variavel_aleatoria_exponencial(taxa):
    return -math.log(1.0 - random.random()) / taxa

def gerador_tempos(n, taxa_chegada=1, taxa_servico=1):
    saida = []
    for i in range(n):
        saida.append([variavel_aleatoria_exponencial(taxa_chegada), variavel_aleatoria_exponencial(taxa_servico), 0])
    
    return saida


def simulador_mm1(taxa_chegada, taxa_servico, precisao):
    tamanho = 5000  #tamanho e inicial e que vai ser acrescido quando houver estouro de memória
    tempos_aleatorios = np.array([variavel_aleatoria_exponencial(taxa_chegada), variavel_aleatoria_exponencial(taxa_servico), 0], dtype=np.float32)
    fila = []        #onde esperam
    atendidos = np.zeros(tamanho, dtype=np.float16)     #terminaram o atendimento
    em_servico = tempos_aleatorios
    clock = em_servico[0]
    chegada, servico, espera, soma = 0.0, 0.0, 0.0, 0.0
    iterador = 0

    while True:
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
            soma += em_servico[2]
            em_servico = fila.pop(0)
            em_servico[2] = clock-em_servico[2]
            iterador += 1

        elif em_servico[1] < chegada:
            clock += em_servico[1]
            chegada -= em_servico[1]
            atendidos[iterador] = em_servico[2]
            soma += em_servico[2]
            iterador += 1

            if fila:
                em_servico = fila.pop(0)
                em_servico[2] = clock - em_servico[2]

            else:
                clock += chegada
                em_servico = [chegada, servico, espera]

        elif fila:
            clock += em_servico[1]
            atendidos[-1] = em_servico[2]
            soma += em_servico[2]
            em_servico = fila.pop(0)
            em_servico[2] = clock - em_servico[2]

        if iterador > 2 and iterador%1000 == 0:
            print(iterador)
            intervalo, h = intervalo_de_confianca(atendidos[:iterador], soma/iterador, 95)
            print(f'h é {h}')

            if h/(soma/iterador) <= precisao:
                print(h/(soma/iterador))
                return atendidos, soma, iterador, intervalo



tempos = simulador_mm1(10**5, 9, 10)
print(f'Valor de espera segundo teoria das filas = {9/10}')
print(f'Intervalo de Confiança = {intervalo_de_confianca(tempos, 95)}')
end = time.time()
print(f'Tempo de execução = {end-start} segundos')
print(f'Media de espera na fila = {sum(tempos)/len(tempos)}')