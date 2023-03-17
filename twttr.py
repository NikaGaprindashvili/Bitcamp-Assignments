# Asks user to input something
text = input("Input: ")

# prints Output
print("Output: ", end="")

# creates letter variable which belongs to text, 
# if letter contains vowels, it removes them and gives output without vowels, 
# if letter don't contain vowels it prints same thing as input
for letter in text:
    
    if not letter.lower() in ["a", "e", "i", "o", "u"]:    
     print (letter, end="")

