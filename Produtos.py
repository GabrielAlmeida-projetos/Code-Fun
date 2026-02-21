# Estrutura e algoritmo

# Lista 1
pizzas = [
    "Mussarela",
    "Calabresa", 
    "Doce",
    "Vegetariana", 
    "Frango", 
    "Napollitana",
    "Marguerita",
    "Pepperoni",
    "Atum"  ]
pizzas.sort() # Ordenando as pizzas

# Lista 2
precos = [
    40,
    35,
    45,
    38,
    42,
    39,
    41,
    44,
    50,
    37   ]

precos.sort() # Ordenando os preços

#Printando oque tem Acima de 40
####################################

print("Sabor da pizza e valor \n")

for preco in precos:
    if preco <= 40:
        print(f"Preço: R${preco}")

print("")

#Printando oque tem Acima de 40
####################################

print("Sabor da pizza e valor \n")

for i, pizza in enumerate(pizzas):
    if precos[i] <= 40:
        print(f"{pizza} Custa R${precos[i]} Reais")

print("")


# Tuplas

produtos = [
    ("Placa mãe", 2500),
    ("Mouse", 250),
    ("teclado", 350),
    ("Monitor 1", 850),
    ("monitor 2", 980),
    ("placa de video", 1900),
    ("SSD", 500),
    ("memorias ram", 800),
    ("HD", 320)  ]
produtos.sort()

print("Nome do Produto  e  Valorn \n")

for nome, valor in produtos:
        print(f"{nome}: R${valor}")

print("")

produtos = [
    ("Placa mãe", 2500),
    ("Mouse", 250),
    ("teclado", 350),
    ("Monitor 1", 850),
    ("monitor 2", 980),
    ("placa de video", 1900),
    ("SSD", 500),
    ("memorias ram", 800),
    ("HD", 320)  ]
produtos.sort()

print("Nome do Produto e Valor \n")

for nome, valor in produtos:
    if valor >= 1000:
        print(f"Nome do Produto: {nome}: R${valor}")
