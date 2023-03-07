# Asks Person for the name, Person returns Answer, if Person's name is same as it listed below it returns different Greetings, if not it returns i don't know you.

name = input("What is your name? ").title()

if name == "Giorgi":
 print ("Hello, Giorgi")
elif name == "Sandro":
 print ("Hello Sandro, How are you?")
elif name == "Nika":
 print ("Hello Nika, Have a nice day")
elif name == "Oto":
 print ("Hello Oto, Have a good day")
else:
 print ("I don't know you!")

