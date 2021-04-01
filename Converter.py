import time
#Currency Converter
    #converting from any currency to dollar
#Algorithm :
    #give a numbered list with each number representing a currency
    #Prompt user to pick a number and store that into a variable 
        #if the user does not put a number display error message
    #do the math for it based on the currency
    #based on the number do the conversion and print out statement

def start():
    value = True
    
    while value == True:
        print("\nDisplayed are the different conversion options : What do you want to convert?\nChoose a number.")
        user = input("1) Euro->Dollar\n2) Rupees->Dollar\n3) Yen->Dollar\n4) Pound->Dollar\n5) Franc->Dollar\n6) Canadian Dollar->Dollar\n")
        if user==1:
            print("\nChoice : 1) Euro->Dollar\n")
            time.sleep(2)
            value = False
            currency = "Euros"
        elif user==2:
            print("\nChoice : 2) Rupees->Dollar\n")
            time.sleep(2)
            value = False
            currency = "Rupees"
        elif user==3:
            print("\nChoice : 3) Yen->Dollar\n")
            time.sleep(2)
            value = False
            currency = "Yen"
        elif user==4:
            print("\nChoice : 4) Pound->Dollar\n")
            time.sleep(2)
            value = False
            currency = "Pounds"
        elif user==5:
            print("\nChoice : 5) Franc->Dollar\n")
            time.sleep(2)
            value = False
            currency = "Francs"
        elif user==6:
            print("\nChoice : 6) Canadian Dollar->Dollar\n")
            time.sleep(2)
            value = False
            currency = "Canadian Dollars"
        else:
            print("\nError, please try again.\n")
            time.sleep(0.5)
    
    value2 = True
    while value2 == True:
        amount = input("Enter the amount of {} you want to convert\n".format(currency))
        try:
            amount = float(amount)
            if amount<0:
                print("Invalid input, please enter a non-negative number.\n")
                time.sleep(1)
                value2=True

            else:
                value2 = False
        except ValueError:
            print("Invalid input, please enter a valid number.\n")
            time.sleep(1)

    if currency == "Euros":
        printTotal(1,amount)
    elif currency =="Rupees":
        printTotal(2,amount)
    elif currency=="Yen":
        printTotal(3,amount)
    elif currency =="Pounds":
        printTotal(4,amount)
    elif currency=="Francs":
        printTotal(5,amount)
    elif currency =="Canadian Dollars":
        printTotal(6, amount)
    

def printTotal(number, amount):
    if number==1:
        print("\nConversion Rate : 1 Euro = 1.18 USD")
        time.sleep(2)
        total = amount*1.18
        if amount<=1:
            print("{} Euro = {:.2f} dollars\n".format(amount, total))
            time.sleep(2)
        else:
            print("{} Euros = {:.2f} dollars\n".format(amount,total))
            time.sleep(2)
        runAgain()

    elif number==2:
        print("\nConversion Rate : 1 Rupee = 0.013 USD")
        time.sleep(2)
        total = amount*.013
        if amount<=1:
            print("{} Rupee = {:.2f} dollars\n".format(amount, total))
            time.sleep(2)
        else:
            print("{} Rupees = {:.2f} dollars\n".format(amount,total))
            time.sleep(2)
        runAgain()

    elif number==3:
        print("\nConversion Rate : 1 Yen = 0.0094 USD")
        time.sleep(2)
        total = amount*.0094
        print("{} Yen = {:.2f} dollars\n".format(amount,total))
        time.sleep(2)
        runAgain()

    elif number==4:
        print("\nConversion Rate : 1 Pound = 1.30 USD")
        time.sleep(2)
        total = amount*1.3
        if amount<=1:
            print("{} Pound = {:.2f} dollars\n".format(amount, total))
            time.sleep(2)
        else:
            print("{} Pounds = {:.2f} dollars\n".format(amount,total))
            time.sleep(2)
        runAgain()

    elif number==5:
        print("\nConversion Rate : 1 Franc = 1.10 USD")
        time.sleep(2)
        total = amount*1.1
        if amount<=1:
            print("{} Franc = {:.2f} dollars.\n".format(amount,total))
            time.sleep(2)
        else:
            print("{} Francs = {:.2f} dollars.\n".format(amount,total))
            time.sleep(2)
        runAgain()

    else:
        print("\nConversion Rate : 1 Loonie = 0.75 USD")
        time.sleep(2)
        total = amount*.75
        if amount<=1:
            print("{} Loonie = {:.2f} dollars.\n".format(amount,total))
            time.sleep(2)
        else:
            print("{} Loonies = {:.2f} dollars.\n".format(amount,total))
            time.sleep(2)
        runAgain()


def runAgain():
    again = input("\nWould you like to convert an amount again?\n")
    time.sleep(1)
    if again.lower()=='yes' or again.lower()=='y':
        start()
    elif again.lower()=='no' or again.lower()=='n':
        print("End program.")
    else:
        print("\nInvalid input, please try again")
        runAgain()
        time.sleep(1)
start()
