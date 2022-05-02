#!/usr/bin/env python3
# Created by: Ferdous Sediqi
# Created on: April 5, 2022
# This program asks the user for the numbers using loop
# then, check which number is the greatest and smallest
# and display the answer.


def main():
    print("\033[32m", "In this program we display the Greatest and Smallest number")
    print("from user inputs.")

    # declear an emty array
    numbers = []
    # run loop to ask user for numbers
    while True:
        string_input = input("\033[34m" "Enter a number: ")
        try:
            float_input = float(string_input)

            # append user inputs numbers to an array
            numbers.append(float_input)

            # ask user if they want to continue or not and check input
            try_again = input("Enter y to continue or n to quit: ")
            if try_again == "y":
                continue
            else:
                break
        # display invalid input
        except Exception:
            print("Invalid input. Input was not a number.")
            continue
    # line space
    print("")

    #print smallest and greatest number with different colors  
    print("\033[31m",  "The greatest number is {}".format(max(numbers)))
    print("\033[33m", "The smallest number is {}".format(min(numbers)))


if __name__ == "__main__":
    main()
