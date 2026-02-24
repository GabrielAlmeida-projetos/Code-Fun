import random

jogo = ["pedra", "papel", "resoura"]

jogador1 = random.choices(jogo)
jogador2 = random.choices(jogo)


# jogador1 Vence se
if jogador1 == "pedra" and jogador2 == "tesoura":
    print(f"Jogador1 venceu escolha do jogador1: {jogador1} escolha do jogador2: {jogador2}")
    

elif jogador1 == "papel" and jogador2 == "pedra":
    print(f"Jogador1 venceu escolha do jogador1: {jogador1} escolha do jogador2: {jogador2}")
    

elif jogador1 == "tesoura" and jogador2 == "papel":
    print(f"Jogador1 venceu escolha do jogador1: {jogador1} escolha do jogador2: {jogador2}")
    

# jogador2 Vence se



if jogador2 == "pedra" and jogador1 == "tesoura":
    print(f"Jogador2 venceu escolha do jogador2: {jogador2} escolha do jogador1: {jogador1}")
    

elif jogador2 == "papel" and jogador1 == "pedra":
    print(f"Jogador2 venceu escolha do jogador2: {jogador2} escolha do jogador1: {jogador1}")
    

elif jogador2 == "tesoura" and jogador1 == "papel":
    print(f"Jogador2 venceu escolha do jogador2: {jogador2} escolha do jogador1: {jogador1}")
    
