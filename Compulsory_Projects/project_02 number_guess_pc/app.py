import random

def guess_number(number):
    random_number = random.randint(1, number)
    guess = 0

    while guess != random_number:
        user_guess = input(f"Guess a number between 1 to {number} : ")
        
        if user_guess.strip() == "":
            print("⚠️ Invalid input! Please enter a valid number.")
            continue
        elif not user_guess.isdigit():
            print("⚠️ Invalid input! Please enter a valid number.")
            continue

        guess = int(user_guess)

        if guess > random_number:
            print("❌ Too high. Try again.")
        elif guess < random_number:
            print("❌ Too low. Try again.")
        else:
            print(f"🎉 Yay, congrats! You guessed the number {random_number} correctly!")

guess_number(10)
