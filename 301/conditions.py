import random

# Script Name:                  conditions.py
# Author:                       Michael Sineiro
# Date of latest revision:      12/7/2023
# Purpose:                      various conditionals, all wrapped in a
##########                      fun little menu!
# Execution:                    python3 conditions.py


def ageCheck():
    """
    Checks if the user is an adult, teenager, or child based on their age.
    """
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are an adult")
    elif age >= 13:
        print("You are a teenager")
    else:
        print("You are a child")
    


def compRand():
  """
  Checks if a num is greater than, equal to, 
  or less than a random num between 1-10.
  """
  rand = random.randint(1, 10)
  num = int(input("Enter a num: "))

  if num > rand:
    print(f"Your num ({num}) is greater than ({rand}).")
  elif num == rand:
    print(f"Your num ({num}) is equal to ({rand}).")
  else:
    print(f"Your num ({num}) is less than ({rand}).")


def coolName():
    """
    Checks if the user is a student or employed.
    """
    student = bool(input("Are you a student? (True/False): "))
    jobHaver = bool(input("Are you employed? (True/False): "))

    if student or jobHaver:
        print("I feel ya, bud.")
    elif student and jobHaver: 
        print("Both? Wow!")
    else:
        print("Must be nice!")


def account_balance():
    """
    Checks the user's account status and balance.
    """
    acc = bool(input("Do you have an account? (True/False): "))

    if acc:
        print("Valid input")
    else:
        pass

    if acc:
        balance = float(input("Enter your account balance: "))
        if balance > 0:
            print("You have an account with positive balance")
        else:
            print("You have an account with zero or negative balance")
    else:
        print("You do not have an account")


def main():
    """
    Main function that displays a menu and 
    allows users to choose which function to run.
    """
    print("""
    IF OVERLOAD!!!

    What would you like to do?

    1. Check if you are an adult, teenager, or child.
    2. Compare a num to random one.
    3. Check if you are a student or employed.
    4. Check your account status and balance.
    5. Quit.
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        ageCheck()
    elif choice == "2":
        compRand()
    elif choice == "3":
        coolName()
    elif choice == "4":
        account_balance()
    elif choice == "5":
        print("If'n ya'll come back naow")
        exit()
    else:
        print("Invalid choice. Please try again.")

    print("\n")

    # Run the main function again to keep the menu running
    main()


if __name__ == "__main__":
    main()