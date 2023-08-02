def media_aritmetica(dados):
    soma = 0
    for i in dados:
        soma += i

    return soma/len(dados) if len(dados) > 0 else 0

print(media_aritmetica([]))