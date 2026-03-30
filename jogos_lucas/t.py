
import random

print("bem vindo a o dado")
dados = []

for i in range(3):
    ##repetir algo ou percorrer uma lista for in 
    dados.append(random.randint(1,6))
##quantidade de areas 1,6
##evitando numeros inteiros
print("Resultados", dados)

soma = sum(dados)
##sum soma todos os numeros da lista

media = soma // len(dados)
##conta quantos itens tem len
##dividindo pelos numeros

print("Soma:", soma)
print("Média:", media)
