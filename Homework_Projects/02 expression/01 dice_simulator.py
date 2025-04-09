import random

DICE_SIDES = 6

def roll_dice():
    die1: int = random.randint(1, DICE_SIDES)
    die2: int = random.randint(1, DICE_SIDES)
    total: int = die1 + die2
    print(f"You rolled a {die1} and a {die2} for a total of {total}")

def main():
    die1: int = 10
    print(f"die1 in main() is: {die1}")

    for _ in range(3):
        roll_dice()

    # print(f"die1 in main() is: {die}")
if __name__ == "__main__":
    main()
