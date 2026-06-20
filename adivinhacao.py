import random, time, os

jogada = 0
tentativas = 0
numero = random.randint(1, 100)

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
  
while True:
    limpar()
    print("------- Bem vindo ao jogo da adivinhação! -------")
    print("------------- Digite 200 para sair! -------------")
    print("Sua ultima tentativa foi:", jogada)
    print("Você está em sua", tentativas, "tentativa.")
    jogada = int(input("O computador escolheu um número, tente adivinhar qual é!: "))
    tentativas += 1
    
    if jogada == 200:
        print("Obrigado por jogar!")
        break
    elif jogada == numero:
        print("Parabens, você ganhou! Você acertou em ", tentativas, "tentativas. Reiniciando...")
        time.sleep(3)
        jogada = 0
        tentativas = 0
        numero = random.randint(1, 100)
    elif jogada > numero:
        print("Muito alto, tente um número menor!")
        time.sleep(0.6)
    elif jogada < numero:
        print("Muito baixo, tente um número maior!")
        time.sleep(0.6)
    else:
        print("Inválido")