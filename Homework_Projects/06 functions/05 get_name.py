def get_name(name):
    return f"Hello {name}: How are you?"

if __name__ == "__main__":
    user_input_name = input("Enter your name: ?  ")
    your_name = get_name(user_input_name)
    print(your_name)