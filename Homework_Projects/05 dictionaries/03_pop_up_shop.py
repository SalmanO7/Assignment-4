def pop_price():
    fruits = {
        "apple": 40,
        "Banana": 20,
        "kiwi": 34,
        "Mango": 19,
        "Strawberry": 40
    }
    
    total_price = 0

    print("\nAvailable fruits with prices:")
    for fruit, price in fruits.items():
        print(f"{fruit}: {price} PKR")

    print("\nEnter the quantity for each fruit:\n")
    for fruit, price in fruits.items():
        while True:
            try:
                user_quantity = int(input(f"How many {fruit}s do you want? "))
                if user_quantity < 0:
                    print("Invalid quantity. Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        total_price += price * user_quantity

    return total_price

if __name__ == "__main__":
    total_price = pop_price()
    print(f"\nTotal price of fruits is: {total_price} PKR")
