import random

user_won = 0
Comp_won = 0
draw = 0

options = ["R","P","S"]

while True:
    User_input = input("Type R = Rock/ P = Paper/ S = Scissors or q to quit : ")
    if User_input == "q":
        break

    if User_input not in options:
        continue

    random_nu = random.randint(0,2)

    comp_pick = options[random_nu]
    print("computer picked", comp_pick + ".")

    if User_input.upper() in ["R","Rock","rock"] and comp_pick == "S":
        print("You picked "+ User_input +"/n") 
        print("You Won....!")
        user_won +=1


    elif User_input.upper() in ["P","Paper","paper"] and comp_pick == "R":
        print("You picked " +User_input +"/n")
        print("You Won....!")
        user_won +=1

    elif User_input.upper() in ["S","Scissors","scissors"] and comp_pick == "P":
        print("You picked " +User_input +"/n")
        print("You Won....!")
        user_won +=1

    elif User_input == comp_pick:
        print("You picked " +User_input +"/n")
        print("It's Draw ....!")
        draw +=1

    else:
        print("You Lost..!")
        Comp_won +=1

print("You Won", user_won, "Times..")
print("comp Won", Comp_won, "Times..")
print("draw", draw, "Times..")
print("Thank you...!   Goodbye")
