from bib import *             # importar apenas as funcoes que serao utilizadas


def conta_digitos(numero):
    contador = 0
    while numero != 0:
        numero //= 10
        contador += 1
    return contador

def preenche_digitos(numero):
    numero = str(numero)
    return numero.zfill(8)


def metodo_quadrado_central(z0, quantidade):
    lista = []
    iteracoes = 0
    while iteracoes < quantidade:
        z0 = (z0**2) if conta_digitos(z0**2) < 8 else preenche_digitos(z0**2)
        z1 = str(z0[2:6:])
        z0 = z1
        z1 = int(z1) / 10000.0
        lista.append(z1)
        iteracoes += 1
    
    return lista
    
    
print(metodo_quadrado_central(7182, 5))
        