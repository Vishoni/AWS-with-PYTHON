import random

def generate_number():
    return str(random.randint(1000, 9999))

def calculate_cows_and_bulls(secret, guess):
    cows = sum(1 for s, g in zip(secret, guess) if s == g)
    bulls = sum(1 for g in guess if g in secret) - cows
    return cows, bulls

def play_game():
    secret_number = generate_number()
    attempts = 0
    
    print("Welcome to Cows and Bulls!")
    print("I have generated a 4-digit number. Try to guess it.")
    
    while True:
        guess = input("Enter your 4-digit guess: ")
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        
        attempts += 1
        cows, bulls = calculate_cows_and_bulls(secret_number, guess)
        
        print(f"{cows} cows, {bulls} bulls")
        
        if cows == 4:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
