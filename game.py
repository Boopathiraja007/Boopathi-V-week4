import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("You have to make decisions to find your way out.")

def make_choice(question, options):
    while True:
        print(question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path():
    print("You start walking deeper into the forest.")
    time.sleep(1)
    print("You come across a fork in the path.")
    choice = make_choice("Which path do you choose?", ["Left", "Right"])
    if choice == 1:
        print("You chose the left path. It leads to a river.")
        # Add more story and choices here.
    else:
        print("You chose the right path. It leads to a cave.")
        # Add more story and choices here.

if __name__ == "__main__":
    introduction()
    forest_path()
    