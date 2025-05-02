import random 

less_number = 0.5

def chaotic_counting():
    for i in range(10):
        print(f"Chaotic counting: {i}")
        if done():
            print("Done!", random.random())	
            break
        
def done():
    if random.random() < less_number:
        return True
    else: 
        return False        

if __name__ == "__main__":
    chaotic_counting()
    print("Chaotic counting is done.")