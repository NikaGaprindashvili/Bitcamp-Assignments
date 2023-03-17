# Asks the person to input something.

symbol = input("What is the input string? ")

# outputs different answers for different conditions

if symbol != "":
    print (symbol + " has " + str(len(symbol)) + " characters")
    
else:
    print("Please input something")


         