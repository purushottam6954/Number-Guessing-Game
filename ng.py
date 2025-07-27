import random
top_of_range=input("Enter a Number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range <=0:
        print("Please type a number greater than 0 next time :)")
        quit() 
else:
    print("Please type a number next time!")    
    quit()    
random_number=random.randint(0,top_of_range)
guesses=0

while True:
    user_guess=input("Make a Guess! ")
    if user_guess.isdigit():
        guesses+=1
        user_guess=int(user_guess)
        if user_guess==random_number:
            print("You guessed it right!")
            break
        else:
            if user_guess > random_number:
                print("You were above the number")
            else:
                print("You were below the number")

    else:
        print("Please enter a number Only!")
        continue  
print("You got it in",guesses,"guesses")

    


