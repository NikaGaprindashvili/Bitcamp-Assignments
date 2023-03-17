# Asks the person to input Something, returns different outputs to different greetings.

Greeting = input("Greeting: ").strip().lower()

if Greeting.startswith("hello"):
    print ("$0")
elif Greeting.startswith("h"):
    print ("$20")
else:
    print("$100")