# Ask user if he/she wants to roll a dice
# If yes, roll a dice and print the result
# If no, print "Goodbye"
# If user enters anything other than yes or no, print "Invalid choice"

import random 

def roll_dice():
    return random.randint(1, 6)

def main():
    user_input = input("Do you want to roll a dice? (yes/no): ")
    if user_input == "yes":
        print("You rolled a", roll_dice())
    elif user_input == "no":
        print("Thank you for playing. Goodbye!")
    else:
        print("Invalid choice")  
        main()
    
    
if __name__ == "__main__":
    main()