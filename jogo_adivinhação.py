# O código criará um jogo de adivinhação de números. A máquina escolherá um número aleatório de 1 a 100, e o usuário tentará adivinhar. O menu consistirá em duas opções: iniciar o jogo ou fechar o programa.

import random

def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    print("\n--- Adivinhação de números ---")
    print("OBJETIVO: Tente adivinhar o número secreto entre 1 e 100.")
    
    while True:
        try:
            chute = int(input("Digite o seu chute: "))
            tentativas += 1
            
            if chute == numero_secreto:
                print(f"Parabéns! Você acertou em {tentativas} tentativas!")
                break
            elif chute < numero_secreto:
                print("Seu chute é muito baixo. Tente um número maior.")
            else:
                print("Seu chute é muito alto. Tente um número menor.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

while True:
    print("\n--- MENU DE JOGOS---")
    print("1. Jogar Adivinhação de números")
    print("2. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        jogar_adivinhacao()
    elif escolha == '2':
        print("Até a próxima!")
        break
    else:
        print("Opção inválida. Tente novamente.")
