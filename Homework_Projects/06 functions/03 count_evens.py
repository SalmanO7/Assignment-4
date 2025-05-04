even_numbers = []
def count_even_numbers(number):
    total_even_numbers = 0
    for i in range(1, number + 1):
        if i % 2 == 0:
            even_numbers.append(i)
            if i % 2 == 0:
                total_even_numbers += 1
        else:
            continue
    print(f"Total even numbers: {total_even_numbers}")
    return even_numbers 

user_input = int(input("Enter a number for check even numbers: "))
print(count_even_numbers(user_input))

