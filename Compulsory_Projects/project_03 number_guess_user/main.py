import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(1, x)
        else:
            guess = low
        
        feedback = input(f"Is {guess} too high (H), too low (L),  or correct (C)")
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1

       
    print(f"🎉 Yay, congrats! You guessed the number {guess} correctly!")
computer_guess(10)