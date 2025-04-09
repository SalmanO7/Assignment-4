
num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
operation = input("Enter Operation Sign that you want to do: + , - , / ,* ")

if(operation == "+"):
    print(f"Your result is: {num1 + num2}")

elif(operation == "-"):
    print(f"Your result is: {num1 - num2}")

elif(operation == "/"):
    print(f"Your result is: {num1 / num2}")

elif(operation == "*"):
    print(f"Your result is: {num1 * num2}")
else:
    print("Invalid Operation Sign")    
    