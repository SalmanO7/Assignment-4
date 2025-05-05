def main(number):
    double_number = number * 2
    return double_number

if __name__ == "__main__":
    user_input = int(input("Enter a number for double: "))
    result_double_number = main(user_input)
    print(f"your double number is: {result_double_number}")
    