def welcome():
    print("""
Y'all ready to do some basic ass math?
""")


def calculate():
    operation = input("""
Type the Operation You'd like to Perform
+ for addition
- for subtraction
* for multiplication
/ for division
** for raising to a power
root for finding the nth root of a number
""")

    number_1 = int(input("Enter First Number: "))
    number_2 = int(input("Enter Second Number: "))

    # Addition
    if operation == "+":
        print("{} + {} = " .format(number_1, number_2))
        print(float(number_1 + number_2))

    # Subtraction
    elif operation == "-":
        print("{} - {} = " .format(number_1, number_2))
        print(float(number_1 - number_2))

    # Multiplication
    elif operation == "*":
        print("{} * {} = " .format(number_1, number_2))
        print(float(number_1 * number_2))

    # Division
    elif operation == "/":
        print("{} / {} = " .format(number_1, number_2))
        print(float(number_1 / number_2))
       
    # Powers 
    elif operation == "**":
        print("{} ** {} = " .format(number_1, number_2))
        print(float(number_1 ** number_2))
        
    # Roots
    elif operation == "root":
        print("{} root {} = " .format(number_1, number_2))
        print(number_1 **(1.0/float(number_2)))

    else:
        print("You gotta type in one of the six options, idiot.")

    again()


def again():

    calc_again = input("""
Do you want to calculate again?
Please type "Yes" or "No."
    """)

    if calc_again == "Yes":
        calculate()

    elif calc_again == "No":
        print("Learn how to do math in your head, moron")

    else:
        again()


welcome()
calculate()
