# Asks the person to write file name
filename = input("File name: ").lower()

# splits file name from file type
filetype = filename.split(".")

# gives different outputs for different filetype.
match filetype[1]:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpg") 
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")      
    case "zip":
        print("application/zip")      
    case _:
        print("application/octet-stream")
