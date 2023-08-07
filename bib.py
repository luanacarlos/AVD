from numpy import sort
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



mediana([1,2,3,4,5,5,54,4,2,1,])