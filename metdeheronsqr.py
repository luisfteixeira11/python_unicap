g = float(input("entre com um número: \n"))  # número que será usado para calcular a raiz quadrada
quadrado_quer_saber = int(input("entre com um quadrado perfeito: \n"))
nproximo_de_g = (g+(quadrado_quer_saber/g))/2        # algoritmo baseado no método de Heron para calcular a raiz quadrada de um número próximo
if round(nproximo_de_g**2) == quadrado_quer_saber:       
    print(f"{g} é próximo o suficiente de {int(quadrado_quer_saber**(1/2))} para ser considerado o quadrado de {quadrado_quer_saber}")
else:
    print(f"{g} não é próximo o suficiente de {quadrado_quer_saber**(1/2)} para ser considerado o quadrado de {quadrado_quer_saber}")