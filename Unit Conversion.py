def menu ():
    print("Choose a unit conversion option.")
    print("----------------------------------")
    print("1: Liters to Gallons")
    print("2: Liters to Milliliters")
    print("3: Gallons to Liters")
    print("4: Milliliters to Liters")
    print("5: Quit Program")
    print("----------------------------------")
def get_choice ():
    menu()
    try:
        choice = int(input("Enter a choice: "))
        if choice in range(1,5):
            return choice
        else:
            raise Exception
    except Exception:
        print("\nInvalid choice. Please enter an integer between 1-5.")
    
def liters_to_gallons ():
    print("----------------------------------")
    amount=int(input("Enter Quantity: "))
    calc = amount * 0.264172
    result=format(calc, '.2f')
    print(result, "gallons")
    print("----------------------------------")
    input("Press ENTER to return to menu: ")

def liter_to_milliliters ():
    print("----------------------------------")
    amount=int(input("Enter Quantity: "))
    calc = amount * 1000
    result=format(calc, '.2f')
    print(result, "Milliliters")
    print("----------------------------------")
    input("Press ENTER to return to menu: ")

def gallons_to_liters ():
    print("----------------------------------")
    amount=int(input("Enter Quantity: "))
    calc = amount * 3.7854
    result=format(calc, '.2f')
    print(result, "liters")
    print("----------------------------------")
    input("Press ENTER to return to menu: ")

def milliliters_to_liters ():
    print("----------------------------------")
    amount=int(input("Enter Quantity: "))
    calc = amount / 1000
    result=format(calc, '.2f')
    print(result, "liters")
    print("----------------------------------")
    input("Press ENTER to return to menu: ")

def main ():
   choice = None
   while choice != 5:
       choice = get_choice()
       if choice == 1:
        liters_to_gallons()
       elif choice == 2:
           liter_to_milliliters()
       elif choice == 3:
           gallons_to_liters()
       elif choice == 4:
           milliliters_to_liters()
main()