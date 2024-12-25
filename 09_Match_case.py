# EXERCISE 1 :
# Write a program that uses match-case to print a message based on the day of the week.
# The input will be a string with the day name (e.g., "Monday", "Tuesday", etc.). 

day = str(input("Enter the day of the week: "))
match day.lower():
    case 'monday':
        print("Start of the work in the week...")
    case 'tuesday':
        print("Second woking day in the week...")
    case 'wednesday':
        print("weekend is getting closer...;)")   
    case 'thursday':
        print("2 days left untill weekend...🤩")
    case 'friday':
        print("Last woking day hurrayyy!!!...🥳")
    case 'saturday':
        print("Its weeekend enjoyyy.....😎")
    case 'sunday':
        print("weekend is about to be over....🥲")  
    case _ :
        print("Invalid entry......plz enter only the days of week 🙅🏻")                        


# EXERCISE 2 :
# Create a function that matches an integer and prints whether it is negative, zero, or positive.

num = int(input("Enter the number: "))
match num :
    case num if num<0:
        print("Number is negative......➖")
    case 0 :
        print("Number is zero......0️⃣")
    case num if num > 0 :
        print("Number is positive.......➕")       


