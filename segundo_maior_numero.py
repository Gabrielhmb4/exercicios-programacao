def segundo_maior(lista):
    if len(lista) < 2:
        return None  

    maior = segundo = float('-inf') 

    for numero in lista:
        if numero > maior:
            segundo = maior
            maior = numero
        elif numero > segundo and numero != maior:
            segundo = numero

    if segundo == float('-inf'):
        return None 
    return segundo 
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9] 

segundo_maior(numeros)
