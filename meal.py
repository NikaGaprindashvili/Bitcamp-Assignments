def main():
    # Asking for time
    question = input("What time is it? ")
    
    # Converts time
    time = convert(question)
    
    # if and elif for specific times
    if time >= 7 and time <= 8:
        print("Breakfast time")
    elif time >= 12 and time <= 13:
        print("Lunch time")
    elif time >= 18 and time <= 19:
        print("Dinner time")
     
    
    

    
def convert(time):
    # Splits hours and minutes
    hours, minutes = time.split(":")
    
    # converts string to float
    time_convert = float(minutes) / 60
    return float(hours) + time_convert


if __name__ == "__main__":
    main()