# function that converts dollars into float, percent into float, and returns tip

def main():
    dollars = dollars_to_float(input("How much was the meal? ").replace("$", ""))
    percent = percent_to_float(input("What percentage would you like to tip? ").replace("%", ""))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# function that converts dollars into float
def dollars_to_float(d):
    
    
    return float(d)

# function that converts percent into float
def percent_to_float(p):
    
     
     return float(p)/100

main()