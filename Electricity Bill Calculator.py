def electricity_bill(units_consumed, rate_per_unit, fixed_charge):
    # Calculate total bill
    total_charge = (units_consumed * rate_per_unit) + fixed_charge

    return total_charge

def get_units_consumed():
    while True:
        try:
            units_consumed = float(input("Enter the number of units consumed: "))
            if units_consumed < 0:
                print("For units, enter a non-negative value.")
            else:
                return units_consumed
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_rate_per_unit():
    while True:
        try:
            rate_per_unit = float(input("Enter the rate per unit: "))
            if rate_per_unit <= 0:
                print("Rate per unit should be > 0.")
            else:
                return rate_per_unit
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_fixed_charge():
    while True:
        try:
            fixed_charge = float(input("Enter the meter or fixed governmental charge: "))
            if fixed_charge < 0:
                print("Please enter a non-negative value.")
            else:
                return fixed_charge
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    # Get user input for units consumed, rate per unit, and fixed charge
    units_consumed = get_units_consumed()
    rate_per_unit = get_rate_per_unit()
    fixed_charge = get_fixed_charge()

    # Calculate and display the electricity bill
    total_bill = electricity_bill(units_consumed, rate_per_unit, fixed_charge)
    print(f"Your electricity bill for {units_consumed} units is: {total_bill:.2f} local currency")

if __name__ == "__main__":
    main()
