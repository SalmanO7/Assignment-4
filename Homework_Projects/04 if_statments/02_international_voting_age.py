eligible_age: int = 18
uneligible_age: int = 17

def voting_age_dedectore():
    user_input: int= int(input("Enter your age: "))
    if user_input >= eligible_age:
        print("You are eligible to vote. ")
    elif user_input <= uneligible_age:
        print("You are not eligible to vote. ")
    else:
        print("You are not eligible to vote. ")	
        
if __name__ == "__main__":
    voting_age_dedectore()
    