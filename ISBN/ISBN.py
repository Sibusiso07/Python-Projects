# Creating a function check if the ISBN-10 code is valid or not
def isbn_10(isbn10_number):
    # The code will check if teh code has 10 characters
    if len(isbn10_number) != 10:
        print("ISBN-10 code is Invalid!")
    # If the code is valid then the application will start the varification calculations
    # Definied a variable to hold the total and using the for loop to loop through the first 9 characters of the code
    # The code will check if the characters are digits and if not, then the code is invalid
    else:
        isbn10_total = 0
        for i in range(0, 9):
            if isbn10_number[i].isdigit():
                isbn10_total += int(isbn10_number[i]) * (10 - i)
            else:
                print("ISBN-10 code is Invalid!")
        
        # The last character can either be a digit or the X character
        # If the character is x then the program will add 10 to the total and if it's a digit then it will add that digit to the total    
        if isbn10_number[9].lower() == "x":
            isbn10_total += 10
        elif isbn10_number[9].isdigit():
            isbn10_total += int(isbn10_number[9])
        else:
            print("ISBN-10 code is Invalid!")
        
        # The program will try to see if you devide the total by 11, will there be a remainder 
        # If there is no remainder then the code is valid, else the code is invalid
        if isbn10_total % 11 == 0:
            print("Valid")
        else:
            print("Invalid!")

# Creating a function to validate if the ISBN-13 code valid or not
def isbn_13(isbn13_number):
    # Checking if the code has 13 characters.
    if len(isbn13_number) != 13:
        print("ISBN-13 code is Invalid!")
    # If the code has 13 characters then the program will start validating the code
    # The program will define a variable to hold the total and check if the first characker is a digit or not
    # If the first character is a digit the it will be multiplied by 1 and added to the total
    else:
        isbn13_total = 0
        if isbn13_number[0].isdigit():
            isbn13_total += int(isbn13_number[0]) * 1
        else:
            print("ISBN-13 code is Invalid!")
        
        # Using the for loop to go through all the remaining characters of the code.
        # Using the if-else statement to check is each character is a digit and checking if each index is odd or even
        # The digits where the index is odd will be multiplied by 3 and the digits with even indexes will by multiplied by 1
        for i in range(1, 13):
            if isbn13_number[1].isdigit() and i % 2 != 0:
                isbn13_total += int(isbn13_number[i]) * 3
            elif isbn13_number[1].isdigit() and i % 2 == 0:
                isbn13_total += int(isbn13_number[i]) * 1
            else:
                print("ISBN-13 code is Invalid!")
        
        # The program will check if weather is there a remainder when the total is devided by 10
        # If the is no remainder then the code is valid and if there is then the code is invalid.
        if isbn13_total % 10 == 0:
            print("Valid")
        else:
            print("Invalid!")
        
# Creating a loop to ask if the user wished to validate multiple codes
while True:
    # Menu to give the user 3 options to choose from
    menu = input('''Please select from the menu below which ISBN code do you wish to validate:
                10 - ISBN-10
                13 - ISBN-13
                e - Exit
                : ''')
    # If-else statement to choose the appropriate option based on the users choice and call the function appropriate to the user's choice
    if menu == "10":
        isbn10_number = input("\nEnter an ISBN-10 code: ")
        isbn_10(isbn10_number)
    elif menu == "13":
        isbn13_number = input("\nEnter an ISBN-13 code: ")
        isbn_13(isbn13_number)
    elif menu == "e":
        print("Goodbye!")
        break
    else:
        print("\nInvalid input, Please make sure to input according to the menu!\n")