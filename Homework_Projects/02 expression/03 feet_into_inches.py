def main():
    foot:int = 12
    user_feet:int= int(input("Enter the numbers of feet: "))
    inches:int = foot * user_feet
    print(f"{user_feet} feet is equal to {inches} inches")
    
if __name__ == "__main__":
    main()