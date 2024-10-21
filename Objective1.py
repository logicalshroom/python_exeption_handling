# Task 1 Ask the user the temp\

# Task 2 Convert the temp to Celcius. Use a try block to catch errors.

# Task 3 UX: add an else block that displays a nice user output message

# Task 4 Add a finally block to say good bye!


def far_to_cel():
    temp_f = input("Please input the current temp in Farenheit: ")
    try:
        temp_f = int(temp_f) #this is the line that will throw an exception if the data type cant be converted to int
        temp_c = round((( temp_f - 32 ) * 5 / 9), 2)
#        print(temp_c) double checking my math
    except:
        print("Error: Try again, make sure to type an integer!:)")
    else:
        print(f"{temp_f} degress in Farenheit is {temp_c} degrees Celcius.")
    finally:
        print(f"Thanks for using the App! Goodbye!")

far_to_cel()