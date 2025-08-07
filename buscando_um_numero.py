def buscando_um_numero(lista):
  busca = int(input("Número que deseja buscar: "))
  if busca in lista:
    print(f"True")
  else:
    print(f"False") 
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9] 

buscando_um_numero(numeros)
