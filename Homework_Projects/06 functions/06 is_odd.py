
odd_numbers:list = []
def is_number_odd(number):
    for i in range(1, number + 1):
        if i % 2 != 0:
            odd_numbers.append(i)
        else:
            continue
        
if __name__ == "__main__":
    user_input = int(input("Enter a number for check odd numbers:  "))
    is_number_odd(user_input)
    print(f"odd numbers are: {odd_numbers}")
