# Asks user to input something
camel = input("camelCase: ")
snake = ""

# if character contains uppercase letter, it puts _ in front of it and converts uppercase into lowercase letter
for character in camel:
    if character.isupper():
        snake += "_" + character.lower()
    else:
        snake += character

print("snake_case:", snake)

