# Calls for convert function.

def main():
   
    convert()
    
    
# Asks the person for the input, person writes something and adds :) or :(, it converts :) or :( into emojis.
def convert():  

    faces = input("")
    

    faces = faces.replace(":)", "🙂")
    faces = faces.replace(":(", "🙁")

    print (faces)















