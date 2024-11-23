import random

def main():
    
    target_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            
            guess = int(input("Enter a guess: "))

            
            if guess > target_number:
                print("Your guess is too high.")
            elif guess < target_number:
                print("Your guess is too low.")
            else:
                print(f"Congrats! The number was: {target_number}")
                
        except:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
