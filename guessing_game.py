import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0

    print("Bem-vindo ao Jogo de Adivinhação de Números!")
    print("Tente adivinhar um número entre 1 e 100.")

    while True:
        try:
            guess = int(input("Digite seu palpite: "))
            number_of_attempts += 1

            if guess < 1 or guess > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            if guess < number_to_guess:
                print("Muito baixo! Tente novamente.")
            elif guess > number_to_guess:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você adivinhou o número em {number_of_attempts} tentativas.")
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    guessing_game()
