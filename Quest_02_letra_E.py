altura_parede = float(input("Digite a altura: "))
comprim_sala = float(input("Digite o comprimento: "))
largura_sala = float(input("Digite a largura: "))
area_piso = comprim_sala * largura_sala
volume_sala = (largura_sala * comprim_sala * altura_parede)
area_parede = (2 * altura_parede * largura_sala) + (2 * altura_parede * comprim_sala)
print("A quantidade de piso é: ", area_piso, "metros")
print("O volume da sala é: ", volume_sala, "metros")
print("A área das paredes é: ", area_parede, "metros")
