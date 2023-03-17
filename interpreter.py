# Asks the person to input some calculation

expressions = input("Expressions: ")

# splits expressions
x, y, z = expressions.split(" ")

# gives each expression the type
x = float(x)
z = float(z)

# gives y different equation expressions.
match y:

    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)





   

