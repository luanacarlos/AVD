from bib import *             # importar apenas as funcoes que serao utilizadas


def preenche_digitos(numero):
    numero = str(numero)
    return numero.zfill(8)


def trata_numero(numero):
    if len(str(numero)) > 8:
        return str(numero)[:8:]
    else:
        return str(numero)


def metodo_quadrado_central(z0, quantidade):
    lista = []
    iteracoes = 0
    while iteracoes < quantidade:
        z0 = trata_numero((z0**2)) if len(str(z0**2)) >= 8 else preenche_digitos(z0**2)
        z1 = str(z0[2:6:])
        z0 = int(z1)
        z1 = int(z1) / 10000.0
        lista.append(z1)
        iteracoes += 1
    
    return lista
    
    
def gerador_linear_congruencial():
    
    
print(metodo_quadrado_central(1234, 30))

        