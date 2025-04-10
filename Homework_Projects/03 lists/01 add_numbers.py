def add(numbers: list[int]) -> int:
    total = 0
    for i in numbers:
        total += i
    return total

def main():
    numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
    
    total = add(numbers)
    print(f"The total is {total}.")

if __name__ == "__main__":
    main()
    
     