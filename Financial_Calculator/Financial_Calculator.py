# This is a fincial calculator.
#The program will now print the description of what it calculates.
print("Please choose either investment or bond in order to proceed. \n") 
print("Investment - to calculate the amound of interest you'll earn on interest.")
print("Bond - to calculate the amount you'll have to pay on a home loan. \n")

# The program will now ask the user to choose between the 2 options it gave.
fin_cal = input("Please enter which calculations would you like to proceed with (Investment or Bond): ").lower()

# If 'investment is chosen, the program will ask the user to fill in the required information fo the calculations.
if fin_cal == "investment":
    principle_amount = int(input("Please enter the amount you're depositing: "))
    interest_rate = float(input("Please enter the interest rate: "))
    years = int(input("Please enter the number of years for the investment: "))

# The user will now have to choose which interest type do they want, simple or compound.
    interest_type = input("Please enter which type of interest you would like (simple or compound): ").lower()

# The program will now do calculations for either simple interest or compound interest, based on the user's choice.
# The first calculations are for simple interest and print the total investment.
    if interest_type == "simple":
        total_amount = principle_amount * (1 + (interest_rate / 100) * years)
        print("R" + str(total_amount))
# The following calculations are for compound interest and print the total investment.
    elif interest_type == "compound":
        total_amount = round(principle_amount * ((1 + (interest_rate / 100)) ** years))
        print("R" + str(total_amount))
# If the user writes anything besides what was given or submits an empty form, the program will print the following.
    else:
        print("Please be sure to enter either 'simple' or 'compound'.")

# In case bond was chosen intead of investment, the program will ask the user to fill in the required data.
elif fin_cal == "bond":
    house_value = int(input("Please enter the current value of the house: "))
    interest_rate = float(input("Please enter the interest rate: "))
    months = int(input("Pleaase enter the months in which you wish to repay the bond: "))

# The program will now calculate and print the monthly fee.
    monthly_fee = round(((interest_rate / 100) * house_value) / (1 - (1 + (interest_rate / 100)) ** (-1 * months)))
    print("R" + str(monthly_fee))

# If the user does not select either 'investment' or 'bond' then the program shall print the following.
else:
    print("Pleaase be sure to enter either 'investment' or 'bond'.")

