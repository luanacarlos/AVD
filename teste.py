import numpy as np
from scipy.stats import chi2


def gerador_linear_congruencial(a, c, m, quantidade):
    if quantidade <= m:
        lista = []
        iteracoes = 0
        while iteracoes < quantidade:
            n =  ((a*iteracoes) + c)%m 
            lista.append(n/m)
            iteracoes += 1
        
        return lista

    else: 
        print('Não é possivel gerar essa quantidade de numeros com os parametros dados')

def chi_squared_test(generator_output, k):
    # Gerar k intervalos igualmente espaçados entre 0 e 1
    intervals = np.linspace(0, 1, k+1)
    
    # Calcular as frequências observadas
    observed_frequencies = np.histogram(generator_output, bins=intervals)[0]
    
    # Calcular as frequências esperadas (uniformemente distribuídas)
    n = len(generator_output)
    expected_frequency = n / k
    
    expected_frequencies = np.array([expected_frequency] * k)
    
    # Calcular a estatística do qui-quadrado
    chi_squared = np.sum((observed_frequencies - expected_frequencies)**2 / expected_frequencies)
    
    # Calcular os graus de liberdade
    df = k - 1
    
    # Encontrar o valor crítico do qui-quadrado para alpha=0.05 e df graus de liberdade
    critical_value = chi2.ppf(0.95, df)
    
    # Comparar o valor calculado de chi_squared com o valor crítico
    if chi_squared < critical_value:
        return "Aceita a hipotese nula. Os números sao aleatórios."
    else:
        return "Rejeita a hipotese nula. Os números nao sao aleatórios."
    
# Parâmetros para o gerador G1
a1 = 12351
c1 = 1
m1 = 2**15
quantidade1 = 10000  # Ajuste a quantidade conforme necessário

# Gerar a sequência de números pseudoaleatórios
output1 = gerador_linear_congruencial(a1, c1, m1, quantidade1)

# Realizar o teste do qui-quadrado
k1 = 10  # Número de intervalos
result1 = chi_squared_test(output1, k1)
print(result1)
